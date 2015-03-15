from generated.ra_code import cip3_protocol_c
from generated.ra_code.vch_c import const
from generated.ra_code.rdt_c import const as rdt_const
from bitconverters import unique_device_number, rtc
from contextlib import contextmanager
from parsers.mclinic import MClinic
from parsers.baselog import Permanent, UiActions, BteAlarms, WirelessLinkStatus, RaBattery
from parsers import LogMetadata
from parsers.fittingdatalog import FittingDataLog
import logging
from xmlgenerator import elem
from datetime import datetime

logging.basicConfig()

DRIVER_NAME = 'MagicHat:Surgery'
DRIVER_VERSION = '0.0.00.0000'


class CR220Error(Exception):
    def __init__(self, code):
        super(CR220Error, self).__init__("Error Code: {0}".format(code))

class CR220(object):
    # Section 3.1.3: Read ROM from 146980-4 Command Interface Protocol V2.1 - mClinic
    MAX_CIP_PAYLOAD_SIZE = 1531
    # Section 9.1.1: Log metadata data block from TP201019A_FWRG_GR200FF_FirmwareReferenceGuide
    LOG_METADATA_SIZE = 21
    LOG_METADATA = {
    #        'PERMANENT': (0x202100, Permanent),
    #       'UI_ACTIONS': (0x7ee000, UiActions),
    #       'BTE_ALARMS': (0x7ee420, BteAlarms),
    #  'WIFI_LINK_STATS': (0x7ee840, WirelessLinkStatus),
    #       'WA_BATTERY': (0x7eec60, RaBattery),
              'MCLINIC': (0x8f6840, MClinic)}

    def __init__(self, cipdevice):
        self._device = cipdevice
        self._wacip = cipdevice.create_channel(const.VCH_1)
        self._whoIsThere_Completed = False

    def WhoIsThere(self):
        """
        Section 3.1.1 WhoIsThere command 217100 Command Interface Protocol v3
        """
        self._wacip.write(cip_command=cip3_protocol_c.const.CIP_WHO_IS_THERE_REQ, data=[])
        response = self._wacip.read(timeout=1)['data']
        self._serial = unique_device_number((chr(x) for x in response[:11]))
        self._hardware = ''.join(chr(x) for x in response[11:14])
        self._firmware = ''.join(chr(x) for x in response[14:24])
        self._whoIsThere_Completed = True
        return self._serial, self._hardware, self._firmware

    @contextmanager
    def ClinicalMode(self):
        self._wacip.write(cip_command=cip3_protocol_c.const.CIP_START_CLINICAL_MODE_REQ, data=[])
        response = self._wacip.read()['data']
        yield

        self._wacip.write(cip_command=cip3_protocol_c.const.CIP_STOP_CLINICAL_MODE_REQ, data=[])
        response = self._wacip.read()['data']

    def GetAllLogs(self, progress=lambda max_bytes, bytes_read: None):
        """
        Reads all the logs from the device, and returns a tuple (UserDataLogs, FittingDataLogs),
        which are xmlgenerator.elem's.

        xmlgenerator's prettyprint is capable of rendering these to XML.
        """
        (addr, parser) = self.LOG_METADATA['MCLINIC']
        fitting_metadata = self._getLogMetaData(addr, self.LOG_METADATA_SIZE)
        max_bytes = fitting_metadata.buffer_size

        def acc(x, _a=[0]):
            _a[0] += x
            return _a[0]
        byteread_progress = lambda additional_bytes: progress(max_bytes, acc(additional_bytes))

        return [elem('None', [], []), self._getFittingDataLogs(fitting_metadata, parser, byteread_progress)]

    def _getFittingDataLogs(self, metadata, parser, byteread_progress):
        metadata, rawdata, parser, rtcstring = self._readRawLogData(metadata, parser, byteread_progress)
        if not self._whoIsThere_Completed:
            self.WhoIsThere()

        return FittingDataLog(
                              drivername=DRIVER_NAME,
                              driverversion=DRIVER_VERSION,
                              serial=self._serial,
                              hardwareversion=self._hardware,
                              firmwareversion=self._firmware,
                              rtctime=rtcstring,
                              localtime=datetime.now(),
                              utctime=datetime.utcnow(),
                              binarylogs = rawdata,
                              metadata = metadata).xml()

    def _readRawLogData(self, metadata, parser, byteread_progress):
        rawdata = self._getLogData(metadata.start, metadata.buffer_size, byteread_progress)
        rtcdata = self._readRam(rdt_const.WAE_RTC_TIMESTAMP_CIP_ADDR_START, rdt_const.WAE_RTC_TIMESTAMP_SIZE)
        return metadata, rawdata, parser, rtc(rtcdata)

    def _getLogData(self, address, length, byteread_progress=lambda read: None):
        data = []
        max_i = int(length / self.MAX_CIP_PAYLOAD_SIZE)
        for i, offset in enumerate(range(0, length, self.MAX_CIP_PAYLOAD_SIZE)):
            d = self._readRom(address + offset, min(length-i*self.MAX_CIP_PAYLOAD_SIZE, self.MAX_CIP_PAYLOAD_SIZE))
            byteread_progress(len(d))
            data.append(d)
        return ''.join(data)

    def _getLogMetaData(self, address, length):
        d = self._readRom(address, length)
        r = LogMetadata(d)
        r.checkCrc()
        return r

    def _readRom(self, address, length):
        addr = [
            (address & 0xFF0000) >> 16,
            (address & 0x00FF00) >> 8,
            (address & 0x0000FF)
            ]
        metadata_length = [
            (length & 0xFF00) >> 8,
            (length & 0x00FF)
            ]
        self._wacip.write(cip_command=cip3_protocol_c.const.CIP_READ_ROM_REQ, data=addr+metadata_length)
        data = self._wacip.read()['data']
        if len(data) == 1 and length != 1 and data[0] > 0:
            raise CR220Error(data[0])

        return ''.join(chr(x) for x in data)

    def _readRam(self, address, length):
        addr = [
            (address & 0xFF0000) >> 16,
            (address & 0x00FF00) >> 8,
            (address & 0x0000FF)
            ]
        metadata_length = [
            (length & 0xFF00) >> 8,
            (length & 0x00FF)
            ]
        self._wacip.write(cip_command=cip3_protocol_c.const.CIP_READ_RAM_REQ, data=addr+metadata_length)

        data = self._wacip.read()['data']
        if len(data) == 1 and length != 1 and data[0] > 0:
            raise CR220Error(data[0])

        return ''.join(chr(x) for x in data)
