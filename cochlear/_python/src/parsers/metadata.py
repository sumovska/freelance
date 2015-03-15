import struct
import crcmod


class LogMetadata(object):
    """
    Documented in section 9.1.1
    """
    def __init__(self, rawdata):
        d = rawdata
        self.rawdata = rawdata
        self.length = struct.unpack('<L', d[0:4])[0]
        self.start = struct.unpack('<L', d[4:8])[0]
        self.buffer_size = struct.unpack('<L', d[8:12])[0]
        self.idx_start = struct.unpack('<H', d[12:14])[0]
        self.idx_end = struct.unpack('<H', d[14:16])[0]
        self.count = struct.unpack('<H', d[16:18])[0]
        self.overwritten = ord(d[18])
        self.crc = struct.unpack('<H', d[19:21])[0]

    def checkCrc(self):
        ccitt = crcmod.predefined.PredefinedCrc('crc-ccitt-false')
        ccitt.update(self.rawdata[:-2])
        if ccitt.crcValue != self.crc:
            raise CrcError()
        
    def __str__(self):
        return '\n'.join('{0}: {1}'.format(k, v) for k, v in self.__dict__.items())
            