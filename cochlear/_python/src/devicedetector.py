import hid
from Queue import Queue
import time
import traceback
import logging
from devices import HidDevice, VchDevice, CipDevice, HidTimeout
from cr220 import CR220
from xmlgenerator import prettyprint
from threading import Thread
import sys
import logging
log = logging.getLogger(__name__)

logging.basicConfig()

COCHLEAR_VID = 0x1f32
CR220_PID = 0x0fb8
CR230_PID = 0x0fb7

VCH_1 = 1

class DeviceDetector(object):
    def __init__(self, vid, pid):
        self._serials = set()
        self._vid = vid
        self._pid = pid

    def poll(self, on_add, on_remove):
        serials = []
        for dev in hid.enumerate(self._vid, self._pid):
            if dev['serial_number'].strip() == '':
                continue
            serials.append((dev['serial_number'], dev['path']))
        serials_set = set(serials)
        if self._serials != serials:
            for x in self._serials:
                if x not in serials:
                    on_remove(self._vid, self._pid, x[0], x[1])
            for x in serials:
                if x not in self._serials:
                    on_add(self._vid, self._pid, x[0], x[1])
        self._serials = serials

last_percentage = None

class DeviceManager(Thread):
    def __init__(self):
        super(self.__class__, self).__init__()
        self._devices = {}
        self._fittingdatalog_filename = 'output.xml'
        self.last_percentage = 0.0
        self.logs = Queue()
        self.logs_taken = False
        self._should_die = False
        self.stuck = False

    def progress(self, total, completed):
        p = 100 * float(completed) / float(total)
        ip = int(p)
        if ip < self.last_percentage:
            self.last_percentage = 0.0
        self.last_percentage = p

    def die(self):
        self._should_die = True

    def has_logs(self):
        return not self.logs.empty()

    def get_logs(self):
        return self.logs.get(block=False, timeout=1)

    def run(self):
        dd = DeviceDetector(
            vid=COCHLEAR_VID,
            pid=CR220_PID)

        while not self._should_die:
            time.sleep(0.1)
            dd.poll(self.added, self.removed)

    def added(self, vid, pid, serial, path):
        self.stuck = False
        try:
            log.info('Vid: %s Pid: %s Serial: %s', vid, pid, serial)
            device = HidDevice(vid, pid, serial, path)
            self._devices[path] = device

            vchdevice = VchDevice(device)
            cipdevice = CipDevice(vchdevice)
            cr220 = CR220(cipdevice)
            d = cr220.WhoIsThere()
            with cr220.ClinicalMode():
                try:
                    userdatalog, fittingdatalog = cr220.GetAllLogs(self.progress)
                    self.logs.put({
                        'whoisthere': d,
                        'userdatalog': userdatalog,
                        'fittingdatalog': prettyprint(fittingdatalog)})
                except Exception, e:
                    log.exception(e)
                    log.warn('Exception ignored')
            self.logs_taken = True
        except HidTimeout:
            self.stuck = True
        except Exception, e:
            log.exception(e)
            log.warn('Exception ignored')

    def removed(self, vid, pid, serial, path):
        self.stuck = False
        self.last_percentage = 0.0
        log.info('CR220 Removed with serial: %s', serial)
        if path in self._devices:
            self._devices[path].close()
            del self._devices[path]

    def close(self):
        for d in self._devices.values():
            d.close()


def main(argv):
    dm = DeviceManager()
    dm.start()

    while not dm.logs_taken:
        time.sleep(0.1)

if __name__ == '__main__':
    main(sys.argv)
