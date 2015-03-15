from __future__ import unicode_literals
from unittest import TestCase
from crf2 import ZIP_PASSWORD, Crf2, Crf2Metadata, Locus, Gender
from cStringIO import StringIO
import zipfile
import json
import os
from datetime import datetime


class test_Crf2_native(TestCase):
    NAME = os.name

    def setUp(self):
        self._metadata = Crf2Metadata(
            name_first='Charlie',
            name_last='\u65e5\u672c\u4eba\u306e\u6c0f\u540d',
            dob=datetime(year=1968, month=2, day=14),
            gender=Gender.MALE,
            locus=Locus.LEFT,
            implant_id='123456',
            implant_partid=50017,
            implant_serial='12341926',
            utc_date=datetime.utcnow(),
            local_date=datetime.now(),
            surgeon='Peppermint Patty',
            surgery='Daisy Hill Puppy Farm')
        self._log = 'the xml log'
        self._crf = Crf2(self._metadata, self._log)


    def test_is_compressed(self):
        """
        CRF files are compressed with a password.
        Unfortunately, the actual format isn't specified (zip files can have nearly any type of compression)
         - So this test only checks that the file is compressed.

        The DAL is less forgiving.
        """
        stream = StringIO()
        self._crf.write(stream)

        self.assertTrue(zipfile.is_zipfile(stream))

    def test_crf_contains_metadata(self):
        expected = [
            'name_first',
            'name_last',
            'dob',
            'version',
            'gender',
            'locus',
            'implant_id',
            'implant_partid',
            'implant_serial',
            'local_date',
            'utc_date',
            'surgery',
            'surgeon']
        expected.sort()

        stream = StringIO()
        self._crf.write(stream)

        with zipfile.ZipFile(stream, 'r') as zf:
            zf.setpassword(ZIP_PASSWORD)
            md = zf.read('metadata.json')

        actual = json.loads(md).keys()
        actual.sort()

        self.assertEqual(expected, actual)

    def test_crf_contains_fittingdata(self):
        expected = self._log

        stream = StringIO()
        self._crf.write(stream)
        with zipfile.ZipFile(stream, 'r') as zf:
            zf.setpassword(ZIP_PASSWORD)
            actual = zf.read('FittingData.xml')

        self.assertEqual(expected, actual)

class test_Crf2_other_platform(test_Crf2_native):
    # Even though the generated file won't be importable via the DAL,
    # test the python code anyway.
    NAME = 'posix' if os.name == 'posix' else 'not posix'

if __name__ == '__main__':
    unittest.main()
