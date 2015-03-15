from parsers.mclinic import MClinic
from datetime import datetime
from xmlgenerator import elem, tightelem, elem_

class FittingDataLog(object):

    def __init__(self, drivername,
                       driverversion,
                       serial,
                       hardwareversion,
                       firmwareversion,
                       rtctime,
                       localtime,
                       utctime,
                       binarylogs,
                       metadata):
        self._drivername = drivername
        self._driverversion = driverversion
        self._serial = serial
        self._hardware = hardwareversion
        self._firmware = firmwareversion
        self._localtime = localtime
        self._utctime = utctime
        self._rtc = rtctime
        self._binarylogs = binarylogs
        self._metadata = metadata

        self._mclinic = MClinic(self._binarylogs, self._metadata)


    def xml(self):
        xml = self._mclinic.xml()
        return elem("fitting_data_log", [('xmlns', "http://www.cochlear.com/Cdi/RaFittingDataLog/3.0"), ('xmlns:xsi', "http://www.w3.org/2001/XMLSchema-instance")],
                    [
                        elem_("cdi", [], [
                            elem("driver", [('name', self._drivername), ('version', self._driverversion)], []),
                            elem("device", [('serialnumber', self._serial), ('hwversion', self._hardware), ('fwversion', self._firmware)], [])
                        ]),
                        elem("log_version", [('content', '1'), ('format', '1')], ()),
                        tightelem("current_local_time", [], (self._localtime.replace(microsecond=0).isoformat(),)),
                        tightelem("current_utc_time", [], (self._utctime.replace(microsecond=0).isoformat(),)),
                        tightelem("current_rtc", [], (self._rtc,)),
                        xml
                    ])
