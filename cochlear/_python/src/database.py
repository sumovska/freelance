from __future__ import unicode_literals
import constants
import appdirs
import json
import os
from calendar import timegm
from datetime import datetime
from time import localtime
from encoders import JsonEncoder
import crf2
import shutil
import logging

log = logging.getLogger(__name__)


class DatabaseError(Exception):
    def __init__(self, msg, key, value):
        Exception.__init__(self, msg)
        self.key = key
        self.value = value

def parse_datetime(value):
    try:
        if 'T' in value:
            d, t = value.split('T')
        else:
            d, t = value, '00:00:00'
        (year, month, day) = d.split('-')
        (hour, minute, second) = t.split(':')
        return datetime(*[int(x, 10) for x in (year, month, day, hour, minute, second)])
    except ValueError:
        raise ValueError("Could not parse datetime: [%s]" % value)
    
class Session(object):
    FIELDS = ('utc_date', 'implant_id', 'filename', 'dob', 'gender', 'locus', 'clinic', 'surgery', 'surgeon', 'name_first', 'impedances', 'profile', 'name_last', 'implant_partid', 'implant_serial')
    __new_identifier = 0
    
    @property
    def selected(self):
        return self._selected
    @selected.setter
    def selected(self, value):
        self._selected = "on" if value else False
        
    @property
    def utc_date(self):
        return self._utc_date
    @utc_date.setter
    def utc_date(self, value):
        if isinstance(value, basestring):
            self._utc_date = parse_datetime(value)
        else:
            self._utc_date = value
            
    @property
    def dob(self):
        return self._dob
    @dob.setter
    def dob(self, value):
        if isinstance(value, basestring) and value != '':
            self._dob = parse_datetime(value).date()
        else:
            self._dob = value
        
    @property
    def implant_serial_options(self):
        return list(self.__data.get_names('implant_serial', implant_id=self.implant_id))
        
    @property
    def implant_serial(self):
        if self._implant_serial:
            return self._implant_serial
        elif len(self.implant_serial_options) == 1:
            self._implant_serial = self.implant_serial_options[0]
        else:
            return self._implant_serial
    @implant_serial.setter
    def implant_serial(self, value):
        self._implant_serial = value
     
        
    def __init__(self, data, **kwargs):
        self.identifier = self.__get_new_id()
        self.selected = False
        self.__data = data
        
        for fld in self.FIELDS:
            if fld in kwargs:
                setattr(self, fld, kwargs[fld])
            else:
                setattr(self, fld, '')
                
        
    def __get_new_id(self):
        Session.__new_identifier += 1
        return Session.__new_identifier
            
    def _utc_to_local(self, utc):
        # UTC times are reliable. (Local times from the fitting data are not...
        # the time-zone offset may have changed) since that time.
        utc_tp = utc.timetuple()
        seconds_since_epoch = timegm(utc_tp)
        local_tp = localtime(seconds_since_epoch)
        year, mon, mday, hour, min, sec, wday, yday, isdst = local_tp
        return datetime(year, mon, mday, hour, min, sec)
            
    def as_dict(self, include_extra=False):
        r = {fld:getattr(self, fld) for fld in self.FIELDS if hasattr(self, fld) or hasattr(self.__class__, fld)}
        r['local_date'] = self._utc_to_local(self.utc_date)
        
        if include_extra:
            r['identifier'] = self.identifier
            r['name_full'] = " ".join((self.name_first, self.name_last))
            r['selected'] = self.selected
            for k in ['clinic', 'surgeon', 'surgery']:
                r[k+'_options'] = list(self.__data.get_names(k))
            r['implant_serial_options'] = self.implant_serial_options

            if len(r['implant_serial_options']) == 1:
                r['implant_serial'] = r['implant_serial_options'][0]
                r['implant_partid'] = self.__data.get_partid_for_serial(r['implant_serial'])
                
                
        # For some reason, CEF3 crashes if a dictionary of integer keys is provided:
        for k, v in r.items():
            if isinstance(v, dict):
                r[k] = {str(kk):vv for kk, vv in v.items()}
        return r

class MagicDatabase(object):
    def __init__(self):
        log.info("Database Initialised")
    
    def load(self, user_data_dir):
        self._user_data_dir = user_data_dir
        self._datafile = os.path.join(user_data_dir, 'data.json')
        self._DATA = {}
        if os.path.exists(self._datafile):
            log.info('Loading data from %s', self._datafile)
            try:
                with open(self._datafile, 'rb') as f:
                    self._DATA = json.loads(f.read())
            except ValueError:
                pass
                
        if not self._DATA:
            log.info('Fresh installation')
            self._DATA = {
                'clinic': {},
                'surgeon': {},
                'surgery': {},
                constants.CR220_MODE: [],
                constants.CRF_MODE: [],
                constants.HISTORY_MODE: []}
                
        log.info('Transforming data')
        for k in constants.VIEW_MODES:
            self._DATA[k] = [Session(self, **x) for x in self._DATA[k]]
        if 'segment1' not in self._DATA:
            self._DATA['segment1'] = {}
        if 'implant_serial' not in self._DATA:
            self._DATA['implant_serial'] = {}
            
        log.info('Indexing data')
        # The following should never be part of the stored data structures: They are indexes
        self._indexes = {}
        for k in constants.VIEW_MODES:
            for item in self._DATA[k]:
                self._indexes[item.identifier] = item
        self._implant_id_to_serials = {}
        
        for k, v in self._DATA['implant_serial'].items():
            self._add_to_implant_id_map(v['implant_id'], k)
                
        log.info('Completed')
        
    def _add_to_implant_id_map(self, implant_id, serial):
        if implant_id not in self._implant_id_to_serials:
            self._implant_id_to_serials[implant_id] = []
        self._implant_id_to_serials[implant_id].append(serial)
        
    def get_partid_for_serial(self, serial):
        return self._DATA['implant_serial'][serial]['implant_partid']
                
    def _save(self):
        if os.path.exists(self._datafile):
            old = self._datafile
            new = self._datafile + '.bak'
            log.debug('Moving %s to %s', old, new)
            shutil.copyfile(old, new)
        log.debug('Now saving database to %s', self._datafile)
        with open(self._datafile, 'wb') as f:
            f.write(json.dumps(self._DATA, indent=2, cls=JsonEncoder))
        log.info('Save completed.')
        
    def save_new(self, name, data):
        key = data[name]
        self._DATA[name][key] = {}
        self._DATA[name][key].update(data)
        self._save()
        
    def get_names(self, group, **kwargs):
        for k, v in self._DATA[group].items():
            log.info('%s: %s', k, v)
            if kwargs:
                for kk, vv in kwargs.items():
                    if v[kk] != vv:
                        continue
            yield k
        
    def add_session(self, mode, session, cr220_serial, fittingdata):
        self._indexes[session.identifier] = session
        
        absolute = os.path.join(self._user_data_dir, session.utc_date.isoformat().replace(':', '-'), cr220_serial, 'fittingdata.xml')
        session.filename = os.path.relpath(
            absolute,
            self._user_data_dir)
        if not os.path.exists(os.path.dirname(absolute)):
            os.makedirs(os.path.dirname(absolute))
        self._DATA[mode].append(session)
        self._save()
        with open(absolute, 'wb') as f:
            f.write(fittingdata)
            
    def get_session(self, id):
        return self._indexes[id]
        
    def get_sessions(self, mode):
        return self._DATA[mode]
        
    def move(self, identifier, old_mode, new_mode):
        session = self._indexes[identifier]
        session.selected = False;
        self._DATA[new_mode].append(session)
        self._DATA[old_mode].remove(session)
        self._save()
        
    def get_session_by_id(self, identifier):
        return self._indexes[identifier]
        
    def get_selected(self, mode):
        return [x for x in self._DATA[mode] if x.selected == "on"]
    
    def set_selected(self, id, value):
        log.info('set_selected(%s, %s)', id, value)
        self._indexes[id].selected = value
        
    def update_value(self, id, key, value):
        log.info('update_value(%s, %s, <redacted>)', id, key)
        setattr(self._indexes[id], key, value)
        self._save()
        
    def address_for_clinic(self, clinic):
        try:
            return self._DATA['clinic'][clinic]['address']
        except KeyError, e:
            raise DatabaseError("No clinic exists with that name", 'clinic', clinic);
        
    def address_for_surgeon(self, surgeon):
        try:
            return self._DATA['surgeon'][surgeon]['address']
        except KeyError, e:
            raise DatabaseError("No surgeon exists with that name", 'surgeon', surgeon)
            
    def get_crf(self, identifier):
        session = self._indexes[identifier]
        path = os.path.join(self._user_data_dir, session.filename)
        d = session.as_dict()
        d['gender'] = d['gender'][0]
        with open(path, 'rb') as f:
            return crf2.Crf2(crf2.Crf2Metadata(**d), f.read())
            
    def add_implant_details(self, implant_id, implant_serials, implant_partids):
        for implant_serial, implant_partid in zip(implant_serials, implant_partids):
            self._DATA['implant_serial'][implant_serial] = {
                'implant_id': implant_id,
                'implant_partid': implant_partid}
            
            self._add_to_implant_id_map(implant_id, implant_serial)
        self._save()
            
    def has_partid(self, segment1):
        return segment1 in self._DATA['segment1']
        
    def get_partid(self, segment1):
        return self._DATA['segment1'][segment1]
    
    def set_partid(self, segment1, partid):
        self._DATA['segment1'][segment1] = partid
        self._save()
