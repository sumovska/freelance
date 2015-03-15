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
Abstract protocol class
"""

# pylint: disable=W0142

import logging


class ProtocolError(Exception):
    '''
    Generic Protocol Error exception
    Each protocol should implement a specific error that is derived from this one
    '''
    pass


class ProtocolTimeout(ProtocolError):
    '''
    Generic Protocol Timeout exception
    Each protocol should implement a specific error that is derived from this one
    '''
    pass


class Protocol(object):
    '''
    Abstract protocol class
    '''
    # The write default keys are added to write method
    write_default_keys = {"timeout": 10.0}
    # The write needed keys are required in write method
    write_needed_keys = ["data"]
    # The read default keys are added to read method
    read_default_keys = {"timeout": 10.0}
    # The read needed keys are required in read method
    read_needed_keys = []

    # Exception types for protocol
    error = ProtocolError
    timeout = ProtocolTimeout

    # Payload size - if provided all write 'data' keys will be tested for this value
    payload_size = None

    def __init__(self, tag=None, lower=None):
        '''
        Should be called by deriving classes.
        -Creates a logger based on class module name and provided tag.
        -Stores the provided lower layer.
        -Creates instance copies of keys settings:
            write_default_keys, write_needed_keys,
            read_default_keys, read_needed_keys
        @param tag: tag for logging purposes
        @param lower: lower protocol layer
        '''
        self._logger = logging.getLogger(".".join([self.__module__, tag]))
        self._lower = lower
        self.write_default_keys = dict(self.__class__.write_default_keys)
        self.write_needed_keys = list(self.__class__.write_needed_keys)
        self.read_default_keys = dict(self.__class__.read_default_keys)
        self.read_needed_keys = list(self.__class__.read_needed_keys)

    def write(self, **keys):
        '''
        Should be called by write methods in deriving classes
        -Write needed keys are checked based on write_needed_keys
        -Write default keys are added based on write_default_keys
        -'data' key is logged if available
        @note: timeout key is selected as minimum of the default and provided key
        @param keys: a dictionary of provided keys
        @return: updated keys dictionary
        @raise self.error: if needed key is not provided
                           if payload data limit exceeded
        '''
        for key in self.write_needed_keys:
            if key not in keys:
                raise self.error(key + " not provided")
        for key, value in self.write_default_keys.items():
            if key not in keys:
                keys[key] = value
            elif key == "timeout":
                # Propagate the timeout value if it is lower
                keys[key] = min(value, keys[key])
        if self.payload_size is not None and "data" in keys:
            if len(keys["data"]) > self.payload_size:
                raise self.error("Payload data limit exceeded: "
                                 + str(len(keys["data"]))
                                 + "/"
                                 + str(self.payload_size))

        if "data" in keys:
            self._logger.debug("Sending data ("
                               + str(len(keys["data"]))
                               + " bytes)")
        return keys

    def read(self, **keys):
        '''
        Should be called by read methods in deriving classes
        -Read needed keys are checked based on read_needed_keys
        -Read default keys are added based on read_default_keys
        -'data' key is logged if available
        @note: timeout key is selected as minimum of the default and provided key
        @param keys: a dictionary of provided keys
        @return: updated keys dictionary
        @raise self.error: if needed key is not provided
        '''
        for key in self.read_needed_keys:
            if key not in keys:
                raise self.error(key + " not provided")
        for key, value in self.read_default_keys.items():
            if key not in keys:
                keys[key] = value
            elif key == "timeout":
                # Propagate the timeout value if it is lower
                keys[key] = min(value, keys[key])
        if "data" in keys:
            self._logger.debug("Reveiving data ("
                               + str(len(keys["data"]))
                               + " bytes)")
        else:
            self._logger.debug("Receiving data")
        return keys

    def set_lower(self, lower):
        '''
        Changes the lower layer
        @param lower: lower layer that will be used
        '''
        self._lower = lower

    def _read_lower(self, keys):
        '''
        Should be used to issue read requests to the lower layer
        -Calls the read method of lower layer if available
        -Logs 'data' key if returned
        @param keys: a dictionary of keys for the lower layer read method
        @return: keys returned from lower layer read method
        @raise self.error: if lower layer is not available
        '''
        if self._lower is None:
            raise self.error("No lower layer specified - cannot read data")

        return_keys = self._lower.read(**keys)
        if self._logger.isEnabledFor(logging.DEBUG):
            if "data" in return_keys:
                self._logger.debug("Read contents: "
                                   + str(map(hex, return_keys["data"])))
        return return_keys

    def _write_lower(self, keys):
        '''
        Should be used to issue write requests to the lower layer
        -Calls the write method of lower layer if available
        -Logs 'data' key if available
        '''
        if self._lower is None:
            self._logger.debug("Data contents: "
                               + str(keys["data"]))
        elif self._logger.isEnabledFor(logging.DEBUG):
            if "data" in keys:
                self._logger.debug("Write contents: "
                                   + str(map(hex, keys["data"])))

        if self._lower is not None:
            self._lower.write(**keys)

    def set_timeout(self, value):
        '''
        Sets the default timeouts of protocol
        -sets both the timeout value in both read_default_keys and write_default_keys
        '''
        self.read_default_keys["timeout"] = value
        self.write_default_keys["timeout"] = value

    def disconnect(self):
        '''
        Should be called by deriving class disconnect method
        -Disconnects the lower layer if available
        '''
        if self._lower is not None:
            self._lower.disconnect()

    def connect(self):
        '''
        Should be called by deriving class connect method
        -Connects the lower layer if available
        '''
        if self._lower is not None:
            self._lower.connect()

    def is_connected(self):
        '''
        Should be called by deriving class is_connected method
        Tests if connection is established
        @return: connection state of the lower layer if available
                 True if lower layer is not available
        '''
        if self._lower is not None:
            return self._lower.is_connected()
        return True
