#! /usr/bin/env python

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

"""
CIP protocol implementation
"""

import collections
import time

from cochlear.protocols.protocol import ProtocolError, ProtocolTimeout, \
    Protocol


class CipError(ProtocolError):
    pass


class CipTimeout(ProtocolTimeout):
    pass


class Cip(Protocol):
    '''
    Protocol class for CIP protocol

    The protocol requires an additional cip_command key provided when writing
    A cip_command key is also returned when successful reading is done
    '''
    write_needed_keys = ["data", "cip_command"]
    error = CipError
    timeout = CipTimeout

    HEADER_SIZE = 3

    def __init__(self, tag=None, lower=None, max_size=None):
        '''
        @param tag: tag for logging purposes
        @param lower: lower protocol layer
        @param max_size: maximum size of cip packets - if not provided the payload size
                         of lower layer will be used
        @raise CipError: if lower layer has insufficient payload size
        '''
        Protocol.__init__(self, tag, lower)
        self._data_buffer = collections.deque()
        if self._lower is not None and self._lower.payload_size is not None:
            if max_size is not None:
                if self._lower.payload_size < max_size:
                    raise self.error("Lower layer has insufficient payload size")
                else:
                    self.payload_size = max_size - self.HEADER_SIZE
            else:
                self.payload_size = self._lower.payload_size - self.HEADER_SIZE
        elif max_size is not None:
            self.payload_size = max_size - self.HEADER_SIZE
        else:
            self.payload_size = None

    def write(self, **keys):
        '''
        Send CIP frame to the lower layer
        keys used: data, cip_command
        '''
        keys = Protocol.write(self, **keys)

        data = keys["data"]
        data = [keys.pop("cip_command"), 0, 0] + data
        data[1:3] = len(data) >> 8, len(data) & 0xFF

        self._logger.debug("Sending frame ("
                           + str(len(data))
                           + " bytes)")

        keys["data"] = data
        self._write_lower(keys)

    def read(self, **keys):
        '''
        Processes message for the upper layer
        return keys: data, cip_command

        The lower layer can return fragmented data - multiple read attempts will be made
        If a received data fragment is longer than required the extra data will be dumped

        @raise CipError: if wrong header received
        @raise CipTimeout: if timeout occured
        '''
        keys = Protocol.read(self, **keys)
        timeout = keys["timeout"]
        self._logger.debug("Receiving frame)")

        start_time = time.time()
        end_time = start_time + timeout
        time_left = 1

        return_keys = {}
        i = 0
        cip_length = 0
        cip_length_available = False
        cip_command = 0
        cip_data = []

        while time_left:
            time_left = max(end_time - time.time(), 0)
            keys["timeout"] = time_left
            if not self._data_buffer:
                if not cip_length_available or i < cip_length:
                    return_keys.update(self._read_lower(keys))
                    self._data_buffer.extend(return_keys["data"])
            if i == 0:
                cip_command = self._data_buffer.popleft()
                if not (cip_command & 0x80):
                    raise self.error("Wrong CIP header received")
                i += 1
            elif i == 1:
                cip_length = self._data_buffer.popleft() << 8
                i += 1
            elif i == 2:
                cip_length += self._data_buffer.popleft()
                i += 1
                cip_length_available = True
            elif i >= cip_length:
                self._data_buffer.clear()
                break
            else:
                data_to_read = min(len(self._data_buffer), cip_length - i)
                for _ in range(data_to_read):
                    cip_data.append(self._data_buffer.popleft())
                i += data_to_read
                if i >= cip_length:
                    self._data_buffer.clear()
                    break

        if timeout and not time_left:
            raise self.timeout

        return_keys["data"] = cip_data
        return_keys["cip_command"] = cip_command
        return return_keys

    def set_lower(self, protocol):
        '''
        Changes the lower protocol layer:
        payload size will be updated if required
        '''
        self._lower = protocol
        if self._lower is not None and self._lower.payload_size is not None:
            self.payload_size = self._lower.payload_size - self.HEADER_SIZE
