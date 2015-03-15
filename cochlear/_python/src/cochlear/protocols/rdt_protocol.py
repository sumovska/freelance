######################################################################
#
# Company Confidential. Copyright (c) Cochlear Limited 2012.
#
# $Change: 232759 $
# $Revision: #4 $
# $DateTime: 2014/05/21 17:56:59 $
# Authors: Pawel Plesnar
# References:
#
#######################################################################

'''
RDT protocol implementation
'''

import collections
import threading
import time

from cochlear.protocols.protocol import ProtocolError, ProtocolTimeout, \
    Protocol


class RdtProtocolError(ProtocolError):
    pass


class RdtProtocolTimeout(ProtocolTimeout):
    pass


class RdtProtocol(Protocol):
    '''
    Protocol class for RDT protocol
    -The 'send' function should be used instead of 'read' and 'write'
    -'send' must be provided with the following keys:
        rdt_commands -> a list of RDT command objects
    '''
    write_default_keys = {"timeout": 10,
                          "rdt_offset": 1,
                          "cip_command": 0x71}
    write_needed_keys = ["rdt_commands"]
    read_needed_keys = ["rdt_commands"]
    error = RdtProtocolError

    def __init__(self, tag=None, lower=None):
        '''
        @param tag: tag for logging purposes
        @param lower: lower protocol layer
        '''

        Protocol.__init__(self, tag, lower=lower)
        self._data_buffer = collections.deque()
        if lower is not None:
            self._max_size = lower.payload_size
        self._write_buffer = []
        self._write_offset = 0
        self._commands_buffer = []
        self._commands_len = 0
        self._response_len = 0
        self._mutex = threading.Lock()

    def send(self, **keys):
        '''
        Sends and receives a list of rdt_commands
        @return: list of rdt responses
        '''
        responses = []
        self._mutex.acquire()
        try:
            keys = Protocol.write(self, **keys)
            self._write_offset = None
            rdt_commands = keys["rdt_commands"]

            for command in rdt_commands:
                self._parse_command(keys, command)
            # Send buffer if it is not empty
            if self._commands_buffer:
                self._write_buffer.append(self._commands_buffer)

            for commands in self._write_buffer:
                self.write(rdt_commands=commands)
                response = self.read(rdt_commands=commands)
                responses += response["rdt_responses"]
        finally:
            self._mutex.release()
        return responses

    def _parse_command(self, keys, command):
        '''
        Parses a given command and puts it into the write buffer
        '''
        if self._write_offset is None:
            self._write_offset = keys["rdt_offset"]
            self._write_buffer = []
            self._commands_buffer = []
            self._commands_len = 0
            self._response_len = 0
        cmd_length = command.get_size(self._write_offset)
        response_length = command.get_response_size(self._write_offset)
        self._commands_len += cmd_length
        self._response_len += response_length
        if self._commands_len > self._response_len:
            oversize = self._commands_len - self._max_size
            remainder = cmd_length - oversize
        else:
            oversize = self._response_len - self._max_size
            remainder = response_length - oversize
        if oversize > 0:
            # If there is a command in the buffer and
            # remainder length is <= 20 the split command is moved to another write
            # to prevent cutting off very small chunks
            if self._commands_buffer and remainder <= 20:
                # Add command to the next data
                self._write_buffer.append(self._commands_buffer)
                self._commands_buffer = []
                self._write_offset = keys["rdt_offset"]
                self._commands_len = 0
                self._response_len = 0
                self._parse_command(keys, command)
            else:
                # Add splited command to the existing data
                #    and to the next data
                split_commands = command.split(oversize)
                if split_commands[0] is not None:
                    self._commands_buffer.append(split_commands[0])
                self._write_buffer.append(self._commands_buffer)
                self._commands_buffer = []
                self._write_offset = keys["rdt_offset"]
                self._commands_len = 0
                self._response_len = 0
                self._parse_command(keys, split_commands[1])
        else:
            self._commands_buffer.append(command)
            self._write_offset += cmd_length

    def write(self, **keys):
        '''
        Processes rdt commands for the lower layer
        keys used: rdt_commands, rdt_offset
        '''
        keys = Protocol.write(self, **keys)

        rdt_commands = keys.pop("rdt_commands")
        rdt_offset = keys.pop("rdt_offset")
        data = []
        for command in rdt_commands:
            data += command.get_data(len(data) + rdt_offset)
        keys["data"] = data
        self._write_lower(keys)

    def read(self, **keys):
        '''
        Processes message for the upper layer
        return keys: responses
        '''
        keys = Protocol.read(self, **keys)

        self._logger.debug("Receiving frame)")

        return_keys = {}
        rdt_commands = keys.pop("rdt_commands")
        responses = []

        i = 0

        # using the same commands to process response
        timeout = keys["timeout"]
        end_time = time.time() + timeout
        while True:
            time_left = end_time - time.time()
            if time_left <= 0:
                raise self.timeout
            keys["timeout"] = time_left
            try:
                return_keys.update(self._read_lower(keys))
                break
            except ProtocolTimeout:
                continue
        data = return_keys["data"]
        for command in rdt_commands:
            response = command.response_from_buffer(data, i)
            if response is not None:
                responses.append(response)
                i += response.size

        return {"rdt_responses": responses}

    def set_lower(self, protocol):
        '''
        Changes lower protocol layer
        Payload size is updated from lower layer if required
        '''
        self._lower = protocol
        if self._lower is not None:
            self._max_size = self._lower.payload_size
