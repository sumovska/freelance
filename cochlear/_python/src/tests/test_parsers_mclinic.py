import unittest
from mock import Mock
from parsers import MClinic
from parsers.fittingdatalog import FittingDataLog
from tests.mclinic_sample_data import RAW_MCLINIC
from xmlgenerator import prettyprint, elem
from parsers import LogMetadata
from cStringIO import StringIO
from datetime import datetime
import time
from os.path import dirname
try:
    from numpy.random import randint
except:
    from random import randint

FITTING_DATA_LOGS = dirname(__file__) + '/../../fittingdatalogs/'


class test_parsers_mclinic(unittest.TestCase):
    maxTime = 4.0

    def test_perform_load(self):
        metadata = Mock()
        metadata.idx_start = 0
        metadata.idx_end = 225
        metadata.count = 226
        metadata.overwritten = False
        logs = MClinic(RAW_MCLINIC, metadata)
        xml = prettyprint(logs.xml())

    def test_ensure_mclinic_matches_cditool(self):
        PREFIX = '20141212T155334.535000_MCLINIC.log'
        with open(FITTING_DATA_LOGS + PREFIX + '.metadata.bin', 'rb') as f:
            metadata_bin = f.read()
        with open(FITTING_DATA_LOGS + PREFIX + '.bin', 'rb') as f:
            mclinic_bin = f.read()
        metadata = LogMetadata(metadata_bin)

        logs = FittingDataLog( # Simulate CDITool's values
            drivername='CR200 Cochlear Device Driver',
            driverversion='0.0.99.912',
            serial='1-04-024-0005982',
            hardwareversion='P2 ',
            firmwareversion='0300A11F02',
            rtctime='P1DT5H28M19S',
            localtime=datetime(year=2014, month=12, day=12, hour=15, minute=55, second=32),
            utctime=datetime(year=2014, month=12, day=12, hour=15-11, minute=55, second=32),
            binarylogs=mclinic_bin,
            metadata=metadata)
        elts = logs.xml()
        # The RA was still in mclinic-mode, so reading it interrupted the session: Add the resulting additional session that CDITool saw:
        elts.children[5].children.append(
            elem('mclinic_start', [
                ('lognumber', '2150'),
                ('rtc', 'P1DT5H26M44S'),
                ('bteserialnumber', '1-01-010-3474556'),
                ('btehwversion', 'D08'),
                ('btefwversion', '0202C13F03'),
                ('btecipversion', '0.0.3'),
                ('btelogcontentversion', '20213'),
                ('btelogformatversion', '20213'),
                ('rafwversion', '0300A11F02'),
                ('racipversion', '0.0.3')], ()))
        elts.children[5].children.append(
            elem('mclinic_stop', [
                ('lognumber', '2151'),
                ('rtc', 'P1DT5H28M19S'),
                ('bteserialnumber', '1-01-010-3474556'),
                ('btehwversion', 'D08'),
                ('btefwversion', '0202C13F03'),
                ('btecipversion', '0.0.3'),
                ('btelogcontentversion', '20213'),
                ('btelogformatversion', '20213'),
                ('rafwversion', '0300A11F02'),
                ('racipversion', '0.0.3'),
                ('reason', 'USER_EXIT')], ()))
        xml = prettyprint(elts)

        with open(FITTING_DATA_LOGS + '15A.xml', 'wb') as f:
            f.write(xml)

        with open(FITTING_DATA_LOGS + "15A_CDITool.xml", 'rb') as f:
            self.assertEqual(xml, f.read())

    def test_zero_entries(self):
        # This test passes if random data results in no exceptions.
        metadata = Mock()
        metadata.idx_end = metadata.idx_start = randint(0, 225)
        while metadata.idx_end != metadata.idx_start:
            metadata.idx_end = randint(0, 225)
        metadata.count = randint(0, 226)
        metadata.overwritten = randint(0,1)

        # This needs to trigger max_entries = 0 in parsers.baselog.iterate_entries.
        raw = [chr(randint(0, 255)) for _ in range(3)]
        logs = MClinic(''.join(raw), metadata)
        xml = prettyprint(logs.xml())

    def test_random(self):
        # This test passes if random data results in no exceptions.
        metadata = Mock()
        metadata.idx_end = metadata.idx_start = randint(0, 225)
        metadata.count = randint(0, 226)
        metadata.overwritten = randint(0,1)

        def build_random(size):
            s = StringIO()
            i = 0
            max_size = size/10
            while i < max_size:
                # Loop iteration is remarkably slow.
                # Unwind this loop.
                # (Doesn't matter if the loop count is slightly different in this context)
                s.write(chr(randint(0, 255)))
                s.write(chr(randint(0, 255)))
                s.write(chr(randint(0, 255)))
                s.write(chr(randint(0, 255)))
                s.write(chr(randint(0, 255)))
                s.write(chr(randint(0, 255)))
                s.write(chr(randint(0, 255)))
                s.write(chr(randint(0, 255)))
                s.write(chr(randint(0, 255)))
                s.write(chr(randint(0, 255)))
                i += 10
            return str(s)

        raw = build_random(1024*1024*5)

        logs = MClinic(raw, metadata)
        xml = prettyprint(logs.xml())


if __name__ == '__main__':
    unittest.main()
