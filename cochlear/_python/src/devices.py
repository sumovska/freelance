from cochlear.protocols.vch import Vch, VchError
from cochlear.protocols.vch_channel import VchChannel
from cochlear.protocols.cip import Cip
from cochlear.protocols.protocol import Protocol
from generated.ra_code.vch_c import const
import time
import hid
import logging


class HidError(Exception):
    pass


class HidTimeout(HidError):
    pass


class HidDevice(object):
    _report_length = 64
    def __init__(self, vid, pid, serial, path):
        self.vid = vid
        self.pid = pid
        self.serial = serial
        self.payload_size = None # Not known

        self._logger = logging.getLogger(serial)
        self._device = hid.device()
        self._device.open_path(path)
        self._device.set_nonblocking(1)
        self.error = HidError


    def write(self, **keys):
        '''
        Writes data to the HID device
        keys: data - data to be sent

        @raise HidError: if failed to send data
        '''
        data = keys["data"]
        data_stream = "".join(chr(x) for x in data)

        if self._logger.isEnabledFor(logging.DEBUG):
            self._logger.debug("Data contents: %s", str([hex(ord(x)) for x in data_stream]))
        while data_stream:
            if len(data_stream) >= self._report_length:
                hid_report = "".join([chr(0), data_stream[:self._report_length]])
                data_stream = data_stream[self._report_length:]
            else:
                hid_report = "".join([chr(0), data_stream])
                data_stream = ""
            hid_report += chr(0) * (self._report_length + 1 - len(hid_report))
            data_sent = self._device.write([ord(x) for x in hid_report])
            if data_sent < 0:
                raise self.error("Failed to send data!")

    def read(self, **keys):
        '''
        Processes message for the upper layer
            keys: timeout, length
            return keys: data
            raises HidError
        '''
        return_keys = {}
        self._logger.debug("Receiving data: ")
        data = self._read_report(keys["timeout"])
        self._logger.debug("Received frame")
        if self._logger.isEnabledFor(logging.DEBUG):
            self._logger.debug("Frame data: " + str(data))
        return_keys["data"] = data

        return return_keys

    def _read_report(self, timeout):
        '''
        Internal function for HID report reading
        @raise HidError: receiver error
        @raise HidTimeout: reception timeout
        '''
        start_time = time.time()
        while (time.time() - start_time) < timeout:
            data_buffer = self._device.read(self._report_length + 1, 0)
            data_read = len(data_buffer)
            if data_read == self._report_length:
                break
            time.sleep(0.05)
        if data_read != self._report_length:
            raise HidTimeout

        return data_buffer[:self._report_length]

    def close(self):
        self._device.close()

    def __str__(self):
        return 'HidDevice:\n    '+"\n    ".join([
            self._device.get_manufacturer_string(),
            self._device.get_serial_number_string()])


class VchDevice(object):
    def __init__(self, hiddevice):
        self._hiddevice = hiddevice
        self.serial = hiddevice.serial

        self._vch = Vch(
            # The tag is used as an aid for logging: Provide the serial for simplicity.
            tag=self.serial,
            lower=self._hiddevice,
            max_size=const.VCH_FRAME_PLD_MAX_SIZE)

    def create_channel(self, channel_number):
        return VchChannel(
            tag=self.serial,
            lower=self._vch,
            channel=channel_number)


class CipChannel(object):
    def __init__(self, cip):
        self._cip = cip

    def getCIPLength(self):
        return self.getU16(self.CIPlength)

    def write(self, **kwargs):
        return self._cip.write(**kwargs)

    def read(self, **kwargs):
        return self._cip.read(**kwargs)


class CipDevice(object):
    def __init__(self, vchdevice):
        self._vchdevice = vchdevice

    def create_channel(self, channel_number):
        return CipChannel(Cip(
            tag=self._vchdevice.serial,
            lower=self._vchdevice.create_channel(channel_number)))
