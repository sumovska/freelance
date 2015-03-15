import unittest
import os.path
from datetime import datetime
from parsers.fittingdatalog import FittingDataLog
from parsers.metadata import LogMetadata
from xmlgenerator import prettyprint

DRIVER_NAME = 'MagicHat:Surgery'
DRIVER_VERSION = '0.0.00.0000'

class Test_FittingDataLogs(unittest.TestCase):
    def test_loadAllFittingLogs(self):
        binaries = {}
        for entry in os.listdir('.'):
            if os.path.isfile(entry):
                if len(entry.split('_')) == 2:
                    dt, bin = entry.split('_')
                    binaries[dt] = binaries.get(dt, [])
                    binaries[dt].append(bin)

        self._serial = 'foo'
        self._hardware = 'bar'
        self._firmware = 'baz'
        rtcstring='an rtc string'


        for k in binaries.keys():
            mclinic_filename = '{0}_MCLINIC.log.bin'.format(k)
            metadata_filename = '{0}_MCLINIC.log.metadata.bin'.format(k)
            if not os.path.isfile(mclinic_filename) or not os.path.isfile(metadata_filename):
                continue

            with open('{0}_MCLINIC.log.bin'.format(k), 'rb') as f:
                mclinic = f.read()
            with open('{0}_MCLINIC.log.metadata.bin'.format(k), 'rb') as f:
                rawmetadata = f.read()
            metadata = LogMetadata(rawmetadata)
            
            fdl = FittingDataLog(
                drivername=DRIVER_NAME, 
                driverversion=DRIVER_VERSION, 
                serial=self._serial, 
                hardwareversion=self._hardware, 
                firmwareversion=self._firmware, 
                rtctime=rtcstring, 
                localtime=datetime.now(), 
                utctime=datetime.utcnow(),
                binarylogs = mclinic,
                metadata = metadata).xml()
            with open('{0}_FittingDataLog.xml'.format(k), 'wb') as f:
                f.write(prettyprint(fdl))

if __name__ == '__main__':
    unittest.main()
