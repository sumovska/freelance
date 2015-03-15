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
HID transceiver protocol implementation
"""

import sys
import logging
import time
from ctypes import wstring_at

from cochlear.protocols.protocol import ProtocolError, ProtocolTimeout, \
    Protocol

if sys.platform.startswith('win'):
    import cochlear.protocols.drivers.pyhidapi.pyhidapi_win as pyhidapi
elif sys.platform.startswith('linux'):
    import cochlear.protocols.drivers.pyhidapi.pyhidapi_linux as pyhidapi
elif sys.platform.startswith('darwin'):
    import cochlear.protocols.drivers.pyhidapi.pyhidapi_mac as pyhidapi
else:
    raise Exception("HID driver not available for current OS")


class HidError(ProtocolError):
    pass


class HidTimeout(ProtocolTimeout):
    pass


class Hid(Protocol):
    '''
    Transceiver for USB HID
    '''
    error = HidError
    timeout = HidTimeout

    __dev = None
    RA_VID = 0x1F32
    RA_PID = 0x0FB7
    RA_REPORT_LENGTH = 64
    __report_length = RA_REPORT_LENGTH

    open_devices = set()

    def __init__(self, tag, vid, pid, serial=None):
        '''
        Creates a transceiver to device with specific vid, pid and serial number.
        If serial number is not provided, first device will be connected.
        @param tag: tag for logging purposes
        @param vid: 16-bit integer specifying device USB vendor ID
        @param pid: 16-bit integer specifying device USB product ID
        @param serial: optional serial number string
        '''
        Protocol.__init__(self, tag, None)

        self.disconected = True
        self.__serial_number = serial
        self.__vid = vid
        self.__pid = pid
        self.__buffer = []

    @classmethod
    def create_ra_transceiver(cls, tag=None, serial=None):
        '''
        Creates a transceiver to device with specific vid, pid and serial number.
        If serial number is not provided, first device will be connected.
        @param tag: tag for logging purposes
        @param serial: optional serial number string
        '''
        return Hid(tag, cls.RA_VID, cls.RA_PID, serial)

    @classmethod
    def get_available_devices(cls, vid=0, pid=0):
        '''
        Returns a list of information about connected HID devices with selected VID and PID.
        If no VID and PID are specified all HID devices will be returned
        @param vid: optional 16-bit integer specifying device USB vendor ID
        @param pid: optional 16-bit integer specifying device USB product ID
        '''
        device_object = pyhidapi.hid_enumerate(vid, pid)
        device_iter = device_object
        devices_list = []
        while device_iter is not None:
            serial = str(wstring_at(int(device_iter.serial_number)))
            vid = device_iter.vendor_id
            pid = device_iter.product_id
            devices_list.append({"serial": serial,
                                 "vid": vid,
                                 "pid": pid})
            device_iter = device_iter.next
        pyhidapi.hid_free_enumeration(device_object)
        return devices_list

    @classmethod
    def get_available_ras(cls):
        '''
        Returns a list of serial numbers of connected RAs
        Serial numbers can be used to initialize the Transceiver
        '''
        devices_list = Hid.get_available_devices(cls.RA_VID, cls.RA_PID)
        return [x["serial"] for x in devices_list]

    @classmethod
    def restart_hidapi(cls):
        '''
        Restarts the whole hidapi and reconnects opened devices
        This method should be used in mac OSX to create stable communication
        after a software reset.
        '''
        pyhidapi.hid_exit()
        for device in Hid.open_devices:
            vid = device.__vid
            pid = device.__pid
            serial = device.__serial_number
            pyhidapi.hid_open_char(vid, pid, serial)

    def connect(self):
        '''
        Establishes connection with device
        @note: connect is called automatically when using send, receive and get_serial methods
        @raise HidError: if device cannot be opened
        '''
        if self.disconected:
            if self.__serial_number is None:
                self.__dev = pyhidapi.hid_open(self.__vid, self.__pid,
                                               self.__serial_number)
            else:
                self.__dev = pyhidapi.hid_open_char(self.__vid, self.__pid,
                                                    self.__serial_number)
            if self.__dev is None:
                raise HidError("Device cannot be opened")
            if self.__serial_number is None:
                self.__serial_number = (pyhidapi.hid_get_serial_number_string_buffer(self.__dev))
                self.__serial_number = str(wstring_at(int(self.__serial_number)))
            Hid.open_devices.add(self)
            self.disconected = False

    def is_connected(self):
        '''
        Test if connection to the device is established
        '''
        return not self.disconected

    def write(self, **keys):
        '''
        Writes data to the HID device
        keys: data - data to be sent

        @raise HidError: if failed to send data
        '''
        keys = Protocol.write(self, **keys)
        data = keys["data"]
        data_stream = "".join(chr(x) for x in data)

        if self._logger.isEnabledFor(logging.DEBUG):
            self._logger.debug("Data contents: %s", str([hex(ord(x)) for x in data_stream]))
        if self.disconected:
            self.connect()
        while data_stream:
            if len(data_stream) >= self.__report_length:
                hid_report = "".join([chr(0), data_stream[:self.__report_length]])
                data_stream = data_stream[self.__report_length:]
            else:
                hid_report = "".join([chr(0), data_stream])
                data_stream = ""
            hid_report += chr(0) * (self.__report_length + 1 - len(hid_report))
            data_sent = pyhidapi.hid_write(self.__dev, hid_report, len(hid_report))
            if data_sent < 0:
                raise self.error("Failed to send data!")

    def read(self, **keys):
        '''
        Processes message for the upper layer
            keys: timeout, length
            return keys: data
            raises HidError
        '''
        keys = Protocol.read(self, **keys)
        return_keys = {}
        self._logger.debug("Receiving data: ")
        data = self.__read_report(keys["timeout"])
        self._logger.debug("Received frame")
        if self._logger.isEnabledFor(logging.DEBUG):
            self._logger.debug("Frame data: " + str(data))
        return_keys["data"] = data

        return return_keys

    def __read_report(self, timeout=None):
        '''
        Internal function for HID report reading
        @raise HidError: receiver error
        @raise HidTimeout: reception timeout
        '''
        self.connect()
        if timeout is None:
            data_read, data_buffer = pyhidapi.hid_read(self.__dev,
                                                       self.__report_length + 1)
            # TODO: Not sure if error should be raised
            #      maybe just send an empty frame
            if data_read != self.__report_length:
                raise HidError("Receiver error")
        elif timeout == 0:
            data_read, data_buffer = pyhidapi.hid_read_timeout(self.__dev,
                                                               self.__report_length + 1,
                                                               0)
            # TODO: Not sure if error should be raised
            #      maybe just send an empty frame
            if data_read != self.__report_length:
                raise HidError("Receiver error")
        else:
            start_time = time.time()
            while (time.time() - start_time) < timeout:
                data_read, data_buffer = pyhidapi.hid_read_timeout(self.__dev,
                                                                   self.__report_length + 1,
                                                                   0)
                if data_read == self.__report_length:
                    break
                time.sleep(0.05)
            if data_read != self.__report_length:
                raise HidTimeout

        return [ord(x) for x in data_buffer[:self.__report_length]]

    def disconnect(self):
        '''
        Close USB connection
        '''
        if not self.disconected:
            pyhidapi.hid_close(self.__dev)
            Hid.open_devices.remove(self)
            self._logger.info("Transceiver disconnected")
            self.disconected = True

    def get_serial(self):
        '''
        Returns the serial number of device
        @return: serial number string
        '''
        self.connect()
        return self.__serial_number
