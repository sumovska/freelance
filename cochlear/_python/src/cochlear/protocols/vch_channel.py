#! /usr/bin/env python

"""
VCH channel switcher
"""

from cochlear.protocols.protocol import ProtocolError, ProtocolTimeout, \
    Protocol


class VchChannelError(ProtocolError):
    pass


class VchChannelTimeout(ProtocolTimeout):
    pass


class VchChannel(Protocol):
    '''
    Protocol class for single VCH CHANNEL
    -This protocol doesn't add any bytes to the 'data' key
    -vch_channel key is injected for the VCH protocol
    '''
    error = VchChannelError
    timeout = VchChannelTimeout

    def __init__(self, tag=None, lower=None, channel=0):
        Protocol.__init__(self, tag, lower)
        self.channel = channel
        if self._lower is not None and self._lower.payload_size is not None:
            self.payload_size = self._lower.payload_size

    def write(self, **keys):
        '''
        Processes message for the lower layer
            only adds channel key
        '''
        keys = Protocol.write(self, **keys)
        keys["vch_channel"] = self.channel
        self._write_lower(keys)

    def read(self, **keys):
        '''
        Processes message for the upper layer
            only adds channel key
        '''
        keys = Protocol.read(self, **keys)
        keys["vch_channel"] = self.channel
        return self._read_lower(keys)

    def set_lower(self, protocol):
        self._lower = protocol
        if self._lower is not None and self._lower.payload_size is not None:
            self.payload_size = self._lower.payload_size
