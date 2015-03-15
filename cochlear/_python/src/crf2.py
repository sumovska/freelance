import json
import zipfile
import sys
import os
from datetime import datetime
import tempfile
import subprocess
from cStringIO import StringIO
import logging
log = logging.getLogger(__name__)

ZIP_PASSWORD = 'CochlearRem0te'
devnull = open(os.devnull, 'w')

class Gender:
    MALE = 'm'
    FEMALE = 'f'

class Locus:
    LEFT = 'left'
    RIGHT = 'right'
    
class Crf2MetadataEmpty(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        self._kwargs = kwargs

    def dict(self):
        for k in self._kwargs.keys():
            self._kwargs[k] = getattr(self, k)
        return self._kwargs


class Crf2Metadata(Crf2MetadataEmpty):
    def __init__(self, **kwargs):
        kwargs['version'] = '1'
        super(self.__class__, self).__init__(**kwargs)
        self.dob = self.dob.isoformat()
        self.local_date = self.local_date.isoformat()
        self.utc_date = self.utc_date.isoformat()
        assert isinstance(self.name_first, unicode), 'Missing or non-unicode name_first: ' + str(type(self.name_first))
        assert isinstance(self.name_last, unicode), 'Missing or non-unicode name_last'
        assert self.gender in [Gender.MALE, Gender.FEMALE], "Gender is incorrect: %s" % self.gender
        assert self.locus in [Locus.LEFT, Locus.RIGHT], 'Unspecified locus'
        #assert isinstance(self.implant_serial, basestring), 'Missing or non-string implant_serial'
        assert isinstance(self.implant_id, basestring), 'Missing or non-string implant_id'
        #assert isinstance(self.implant_partid, int), 'Missing or non-int implant_partid'
        assert isinstance(self.surgeon, unicode), 'Missing or non-unicode surgeon'
        assert isinstance(self.surgery, unicode), 'Missing or non-unicode surgery'


class Crf2Error(Exception):
    pass

class Crf2(object):
    def __init__(self, crf_metadata=None, fittingdatalog=None):
        self.metadata = crf_metadata
        self.fittingdata = fittingdatalog

    def read(self, stream):
        with zipfile.ZipFile(stream, 'r') as zf:
            self.metadata = Crf2MetadataEmpty(**json.loads(zf.read('metadata.json', ZIP_PASSWORD)))
            self.fittingdata = zf.read('FittingData.xml', ZIP_PASSWORD)
            
    def tostring(self):
        crf = StringIO()
        self.write(crf)
        return str(crf)

    def write(self, stream, osname=os.name):
        td = tempfile.mkdtemp()
        FITTINGDATA_XML = os.path.join(td, 'FittingData.xml')
        METADATA_JSON = os.path.join(td, 'metadata.json')
        CRF = os.path.join(td, 'crf.zip')

        try:
            try:
                r = None
                log.info('Writing fittingdata...')
                with file(FITTINGDATA_XML, 'wb') as f:
                    f.write(self.fittingdata)
                log.info('Writing metadata...')
                with file(METADATA_JSON, 'wb') as f:
                    f.write(json.dumps(self.metadata.dict()))
                log.info('Writing CRF...')
                if osname == "posix":
                    r = subprocess.call(["zip",
                                     "-P", ZIP_PASSWORD,
                                     "-q",
                                     "-j",
                                     CRF,
                                     FITTINGDATA_XML,
                                     METADATA_JSON,
                                 ], stdout=devnull, stderr=devnull)
                else:
                    # Assume windows.
                    if hasattr(sys, '_MEIPASS'):
                        base = sys._MEIPASS
                    else:
                        base = os.path.dirname(__file__)
                    EXE = os.path.join(base, '7z.exe')
                    r = subprocess.call([EXE, "a",
                                     "-p" + ZIP_PASSWORD,
                                     "-tzip",
                                     "-y",
                                     "-w" + td,
                                     CRF,
                                     FITTINGDATA_XML,
                                     METADATA_JSON], stdout=devnull, stderr=devnull)

                log.info('Copying CRF to stream...')
                with file(CRF, 'rb') as f:
                    stream.write(f.read())
            except Exception, e:
                print e
        finally:
            errors = []
            for filename in [FITTINGDATA_XML, METADATA_JSON, CRF, td]:
                if not self._remove_file(filename):
                    errors.append(filename)
            if errors:
                raise Crf2Error('Could not generate CRF2, {0} could not be generated. Subprocess returned {1}'.format(errors, r))


    def _remove_file(self, filename):
        if os.path.exists(filename):
            if os.path.isfile(filename):
                os.remove(filename)
                return True
            else:
                os.rmdir(filename)
                return True
        return False
