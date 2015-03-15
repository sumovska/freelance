#! /usr/bin/env python

'''
RDT security protocol implementation
'''

import collections

from cochlear.protocols.protocol import ProtocolError, ProtocolTimeout, \
    Protocol


class RdtSecurityError(ProtocolError):
    pass


class RdtSecurityTimeout(ProtocolTimeout):
    pass


class RdtSecurity(Protocol):
    '''
    Protocol class for RDT security layer
    -Security word is added to the 'data' key
    -Two security words can be provided and swapped
    '''
    error = RdtSecurityError
    timeout = RdtSecurityTimeout

    def __init__(self, tag=None, lower=None,
                 security_word=None, security_word_2=None):
        '''
        @param tag: tag for logging purposes
        @param lower: lower protocol layer
        @param security_word: primary security word (16-bit integer)
        @param security_word2: secondary security word (16-bit integer)
        '''
        Protocol.__init__(self, tag, lower)
        self._data_buffer = collections.deque()
        self._security_word = security_word
        self._security_word_2 = security_word_2
        if self._lower is not None and self._lower.payload_size is not None:
            self.payload_size = self._lower.payload_size - 2

    def write(self, **keys):
        '''
        Processes message for the upper layer
        adds security word at the beginning of frame
        '''
        Protocol.write(self, **keys)

        data = keys["data"]
        if self._security_word is None:
            raise RdtSecurityError("Security word not provided")
        data = [self._security_word >> 8, self._security_word & 0xFF] + data
        self._logger.debug("Sending frame ("
                           + str(len(data))
                           + " bytes)")
        keys["data"] = data
        self._write_lower(keys)

    def read(self, **keys):
        '''
        Processes message for the upper layer
        only passes the message
        '''
        Protocol.read(self, **keys)
        return self._read_lower(keys)

    def swap_security_word(self):
        '''
        Swaps the security words
        '''
        temp = self._security_word
        self._security_word = self._security_word_2
        self._security_word_2 = temp

    def set_lower(self, protocol):
        '''
        Changes the lower protocol layer
        Updates payload size based on lower layer if required
        '''
        self._lower = protocol
        if self._lower is not None and self._lower.payload_size is not None:
            self.payload_size = self._lower.payload_size - 2
