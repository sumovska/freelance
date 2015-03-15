from __future__ import unicode_literals

from unittest import TestCase

import os
import database
import constants
import re
import json
from mock import Mock
from datetime import datetime, date

TEST_FILENAME = './data.json'
HTML_FILE = './html/index.html'

def mk_Session(db, **kwargs):
    
    year, month, day, hour, minute, second = 2010, 11, 12, 13, 14, 15
    if 'locus' not in kwargs:
        kwargs['locus'] = 'left'
    if 'gender' not in kwargs:
        kwargs['gender'] = 'male'
    if 'utc_date' not in kwargs:
        kwargs['utc_date'] = datetime(year, month, day, hour, minute, second)
    if 'dob' not in kwargs:
        kwargs['dob'] = '1988-07-08'
    r = {x: kwargs[x] if x in kwargs else 'value' for x in database.Session.FIELDS}
    return database.Session(db, **r)

class TestSession(TestCase):
    maxDiff = None
    def testSessionsIdentifier(self):
        db = Mock(database.MagicDatabase)
        db.get_names.return_value = []
        first = mk_Session(db)
        second = mk_Session(db)
        
        self.assertEquals(first.identifier + 1, second.identifier)
        
    def testAsDict(self):
        """
        By default, this is used for serialization.
        """
        session = mk_Session(Mock())
        self.assertTrue('identifier' not in session)
        self.assertTrue('clinic_options' not in session)
        self.assertTrue('surgery_options' not in session)
        self.assertTrue('surgeon_options' not in session)
        
    def testDateFields(self):
        session = mk_Session(Mock(), dob='2014-12-12', date='2014-12-12T12:13:14', utc_date='2014-12-12T05:12:17')
        self.assertTrue(isinstance(session.as_dict()['local_date'], datetime))
        self.assertTrue(isinstance(session.dob, date))
        self.assertTrue(isinstance(session.utc_date, datetime))
        
    def testAsDict(self):
        """
        However, if database has been provided, then it should provide a dict with all needed information.
        """
        db = Mock()
        db.get_names.return_value = ['one', 'two', 'three']
        session = mk_Session(db).as_dict(True)
        self.assertTrue('identifier' in session)
        self.assertTrue('clinic_options' in session)
        self.assertTrue('surgery_options' in session)
        self.assertTrue('surgeon_options' in session)
        
    def test_all_datatypes_handled(self):
        with open(HTML_FILE, 'rb') as f:
            html = f.read()
        
        datatypes = {
            # These two aren't in the index.html, but are still significant:
            'identifier': 21,
            'filename': '',
            'implant_partid': '',
            'impedances': [],
            'implant_serial_options': ['value', 'value'],
            'profile': [],
            'name_full': 'value value',
            'utc_date': datetime(2014, 12, 12, 1, 1, 1),
            'implant_id': 1234123}
        pat = re.compile('data-type="(.*?)"')
        for m in pat.finditer(html):
            key = unicode(m.group(1))
            if key == 'dob':
                datatypes[key] = datetime(1234, 12, 12)
            elif key.endswith('_options'):
                datatypes[key] = ['value', 'value']
            else:
                datatypes[key] = 'value'
            
        
        db = Mock()
        db.get_names.return_value = ['value', 'value']
        expected = database.Session(db, **datatypes).as_dict(True)
        actual = datatypes
        expected['selected'] = 'value'
        expected['local_date'] = 'value'
        expected['identifier'] = actual['identifier']
        self.assertEquals(expected, actual)
        
    def test_all_session_view_modal_ids_handled(self):
        with open(HTML_FILE, 'rb') as f:
            html = f.read()
        
        datatypes = {
            # These two aren't in the index.html, but are still significant:
            'identifier': 21,
            'filename': '',
            'implant_partid': '',
            'impedances': [],
            'implant_serial_options': ['value', 'value'],
            'profile': [],
            'selected': False,
            'utc_date': datetime(2014, 12, 12, 1, 1, 1),
            'implant_id': 1234123}
        pat = re.compile('id="view_modal_(.*?)"')
        for m in pat.finditer(html):
            key = unicode(m.group(1))
            if key == 'dob':
                datatypes[key] = datetime(1234, 12, 12)
            elif key.endswith('_options'):
                datatypes[key] = ['value', 'value']
            else:
                datatypes[key] = 'value'
            
        db = Mock()
        db.get_names.return_value = ['value', 'value']
        expected = database.Session(db, **datatypes).as_dict(True)
        actual = datatypes
        expected['local_date'] = 'value'
        expected['name_full'] = 'value'
        expected['identifier'] = actual['identifier']
        self.assertEquals(expected, actual)
        
    def testAsDict_OptionalFields(self):
        db = Mock(database.MagicDatabase)
        db.get_names.return_value = []
        expected = database.Session(db, utc_date=datetime.now()).as_dict()
        optional = database.Session.FIELDS
        actual = {'utc_date':expected['utc_date'], 'local_date':expected['local_date']}
        actual.update({k:'' for k in optional if k not in actual})
        self.assertEquals(expected, actual)
        
    def testAsDict_OptionalFields_WithDatabase(self):
        db = Mock(database.MagicDatabase)
        db.get_names.return_value = []
        expected = database.Session(db, utc_date=datetime.now()).as_dict(True)
        optional = list(database.Session.FIELDS) + [
            'clinic_options', 'surgery_options', 'surgeon_options', 'implant_serial_options']
        actual = {
            'utc_date':expected['utc_date'],
            'local_date':expected['local_date'],
            'identifier':expected['identifier'],
            'name_full':expected['name_full'],
            'selected':expected['selected']}
        actual.update({k:([] if k.endswith('options') else '') for k in optional if k not in actual})
        
                
        self.assertEquals(expected, actual)
        

class TestDatabase(TestCase):
    maxDiff = None
    def setUp(self):
        self._db = database.MagicDatabase()
        self.session = mk_Session(self._db)
            
    def tearDown(self):
        if os.path.exists(TEST_FILENAME):
            os.remove(TEST_FILENAME)
        if os.path.exists(TEST_FILENAME+'.bak'):
            os.remove(TEST_FILENAME+'.bak')
        if os.path.exists(self.session.filename):  
            os.remove(self.session.filename)
            os.removedirs(os.path.dirname(self.session.filename))
            
    def test_load(self):
        with open(TEST_FILENAME, 'wb') as f:
            f.write('{}')
            
        self._db.load(os.path.dirname(TEST_FILENAME))
        
    def test_save(self):
        self._db.load(os.path.dirname(TEST_FILENAME))
        self._db._save()
        with open(TEST_FILENAME, 'rb') as f:
            self.assertEquals(json.loads(f.read()), {'segment1':{}, 'implant_serial': {}, 'history_view':[],  'cr220_view':[], 'crf_view':[],  'clinic':{}, 'surgeon':{}, 'surgery':{}})
            
    def test_session_without_serials(self):
        self.session = mk_Session(self._db, implant_serial='', implant_partid='')
        self._perform_save_one_session()
        session = self._db.get_sessions(constants.CR220_MODE)[0].as_dict(True)
        expected = ['', '', []]
        actual = [session.get(x, None) for x in ['implant_serial', 'implant_partid', 'implant_serial_options']]
        self.assertEquals(actual, expected)
        
    def test_session_with_one_serial(self):
        self.session = mk_Session(self._db, implant_serial='', implant_partid='')
        self._perform_save_one_session()
        self._db.add_implant_details('value', ['implant_serial'], ['implant_partid'])
        session = self._db.get_sessions(constants.CR220_MODE)[0].as_dict(True)
        expected = ['implant_serial', 'implant_partid', ['implant_serial']]
        actual = [session.get(x, None) for x in ['implant_serial', 'implant_partid', 'implant_serial_options']]
        self.assertEquals(actual, expected)
        
    def test_session_with_multiple_serial(self):
        """
        If multiple serial numbers could match a given implant, then don't automatically set it.
        """
        self.session = mk_Session(self._db, implant_serial='', implant_partid='')
        self._perform_save_one_session()
        self._db.add_implant_details('value', ['implant_serial1', 'implant_serial2'], ['implant_partid1', 'implant_partid2'])
        session = self._db.get_sessions(constants.CR220_MODE)[0].as_dict(True)
        expected = ['', '', ['implant_serial2', 'implant_serial1']]
        actual = [session.get(x, None) for x in ['implant_serial', 'implant_partid', 'implant_serial_options']]
        self.assertEquals(actual, expected)
        
    def _perform_save_one_session(self):
        self._db.load(os.path.dirname(TEST_FILENAME))
        self._db.add_session(constants.CR220_MODE, self.session, 'cr220-serial', 'foo.xml-data')
        self._db._save()
        
    def test_save_one_session(self):
        """
        This effectively tests the minimal schema
        """
        self._perform_save_one_session()
        with open(TEST_FILENAME, 'rb') as f:
            self.assertEquals(json.loads(f.read()), 
                {
                    'history_view':[],
                    'cr220_view':[{
                        'clinic':'value',
                        'surgery':'value',
                        'surgeon':'value',
                        'name_first':'value',
                        'name_last':'value',
                        'impedances':'value',
                        'profile':'value',
                        'implant_serial':'value',
                        'filename':r'2010-11-12T13-14-15\cr220-serial\fittingdata.xml',
                        'dob':'1988-07-08',
                        'local_date':'2010-11-13T00:14:15',
                        'utc_date':'2010-11-12T13:14:15',
                        'implant_id':'value',
                        'implant_partid':'value',
                        'gender':'male',
                        'locus':'left'}],
                    'crf_view':[],
                    'clinic':{},
                    'surgeon':{},
                    'segment1':{},
                    'implant_serial':{},
                    'surgery':{}})
                    
    def test_set_partid(self):
        partid = 'partid'
        segment = 'segment'
        self._db.load(os.path.dirname(TEST_FILENAME))
        self._db.set_partid(segment, partid)
        
        self.assertEquals((self._db.has_partid(segment), self._db.get_partid(segment)), (True, partid))
            
    def test_load_one_session(self):
        self._perform_save_one_session()
        self._db = database.MagicDatabase()
        self._db.load(os.path.dirname(TEST_FILENAME))
        
    def test_set_selected_true(self):
        self._perform_save_one_session()
        id = self._db.get_sessions(constants.CR220_MODE)[0].identifier
        self._db.set_selected(id, True)
        self.assertEquals(self._db.get_selected(constants.CR220_MODE)[0].selected, "on")
        
    def test_set_selected_false(self):
        self._perform_save_one_session()
        id = self._db.get_sessions(constants.CR220_MODE)[0].identifier
        self._db.set_selected(id, False)
        self.assertEquals(0, len(self._db.get_selected(constants.CR220_MODE)))
        
    def test_fittingdatalog_file_is_relative(self):
        self._perform_save_one_session()
        session = self._db.get_sessions(constants.CR220_MODE)[0]
        self.assertFalse(
            session.filename.startswith('.') or
            session.filename.startswith(os.path.dirname(TEST_FILENAME)) or
            (os.path.abspath(session.filename) == session.filename), 'Filename is not relative to data dir: '+session.filename)
        
    def test_crf2_contains_fittingdata(self):
        self._perform_save_one_session()
        session = self._db.get_sessions(constants.CR220_MODE)[0]
        session.implant_partid = 50017
        crf = self._db.get_crf(session.identifier)
        self.assertEquals(crf.fittingdata, "foo.xml-data")