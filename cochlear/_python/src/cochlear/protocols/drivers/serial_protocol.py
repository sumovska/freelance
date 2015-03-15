#! /usr/bin/env python

######################################################################
#
# Company Confidential. Copyright (c) Cochlear Limited 2012.
#
# $Change: 232759 $
# $Revision: #5 $
# $DateTime: 2014/05/21 17:56:59 $
# Authors: Pawel Plesnar
# References:
#
#######################################################################

"""
Serial transceiver protocol implementation
"""

import serial
import logging
import time
from cochlear.protocols.protocol import ProtocolError, Protocol, ProtocolTimeout


class SerialProtocolError(ProtocolError):
    pass


class SerialProtocolTimeout(ProtocolTimeout):
    pass


class SerialProtocol(Protocol):
    '''
    Transceiver for Serial (RS232)
    '''
    read_default_keys = {"timeout": 2.0}

    error = SerialProtocolError
    timeout = SerialProtocolTimeout
    __dev = None
    CP900BAUD = 115200

    __UNIT_TIMEOUT = 0.5

    def __init__(self, tag, port, baudrate, write_delay=None):
        '''
        Creates a transceiver to device on specific port with a selected baud rate.
        @param tag: tag for logging purposes
        @param port: com port string
        @param baudrate: connection baudrate
        @param write_delay: delay in seconds added between each byte send

        '''
        Protocol.__init__(self, tag, None)
        self.baudrate = baudrate
        self.port = port
        self.write_delay = write_delay
        self.__dev = serial.Serial(self.port,
                                   self.baudrate,
                                   timeout=self.__UNIT_TIMEOUT)

    @classmethod
    def create_cp900_transceiver(cls, tag, port, baud=None):
        '''
        Creates a transceiver to a cp900 device.
        @param tag: tag for logging purposes
        @param port: com port string
        @param baudrate: optional connection baudrate (default is 115200)

        @note: a write delay of 0.0005s is added
        '''
        baud = cls.CP900BAUD if baud is None else baud
        return SerialProtocol(tag, port, baud, write_delay=0.0005)

    def connect(self):
        '''
        Establishes connection with device
        @note: connect is called automatically when using send, receive and get_serial methods
        '''
        if not self.__dev.isOpen():
            self.__dev.open()

    def is_connected(self):
        '''
        Test if connection has been established
        '''
        return self.__dev.isOpen()

    def write(self, **keys):
        '''
        Writes data to the rs232
            keys: data - data to be sent

        @raise SerialProtocolError: if not connected
        '''
        keys = Protocol.write(self, **keys)
        data = keys["data"]
        data_stream = "".join(chr(x) for x in data)

        if self._logger.isEnabledFor(logging.DEBUG):
            self._logger.debug("Data contents: "
                               + str([hex(ord(x)) for x in data_stream]))

        if not self.is_connected():
            raise self.error("Serial not connected: call connect()")
        if self.write_delay is None:
            self.__dev.write(data_stream)
        else:
            for i in data_stream:
                start = time.clock()
                self.__dev.write(i)
                end = start + self.write_delay
                while time.clock() < end:
                    pass

    def read(self, **keys):
        '''
        Processes message for the upper layer
            keys: serial_timeout
            return keys: data

        @raise SerialProtocolError: if not connected
        @raise SerialProtocolTimeout: if timeout occured
        '''

        keys = Protocol.read(self, **keys)
        timeout = keys["timeout"]
        start_time = time.time()
        end_time = start_time + timeout
        time_left = 1

        return_keys = {}
        if not self.is_connected():
            raise self.error("Serial not connected: call connect()")
        while time_left:
            data = self.__dev.read()
            if data:
                break
            time_left = max(end_time - time.time(), 0)
        if not data:
            raise self.timeout

        if self._logger.isEnabledFor(logging.DEBUG):
            self._logger.debug("Received byte, value: "
                               + hex(ord(data)))
        return_keys["data"] = [ord(data)]

        return return_keys

    def disconnect(self):
        '''
        Close serial connection
        '''
        self.__dev.close()
