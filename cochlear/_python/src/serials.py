"""
Provides an interface that returns a (potentially cached) set of serial numbers for a given implant.

The following site is useful dev docs:  http://boto.readthedocs.org/en/latest/dynamodb2_tut.html?highlight=dynamodb2
"""
from boto.dynamodb2 import connect_to_region, regions
from boto.dynamodb2.table import Table
from constants import AWS_KEY_ID, AWS_SECRET, AWS_SERIALS_REGION
from threading import Thread
from Queue import Queue
from time import sleep
import logging

log = logging.getLogger(__name__)

_IMPLANTS_TABLE_NAME = 'mh-implants'
_LOOKUP_TABLE_NAME = 'mh-cdm-device-lookup'

class Serials(object):
    def __init__(self, partid_cache):
        self.__partid_cache = partid_cache
        self._connection = connect_to_region(
            AWS_SERIALS_REGION,
            aws_access_key_id=AWS_KEY_ID,
            aws_secret_access_key=AWS_SECRET)
        
    def fetch(self, implant_id):
        log.info('Fetching implant: %s', 'x'*len(implant_id))
        def fetch_implant(implant_instance_id):
            implant = c.get_item(table_name=_IMPLANTS_TABLE_NAME,
                key={'instance_id': {'N': implant_instance_id}})['Item']
            log.info('Got something')
            return {
                'implant_serial': str(implant['serial_number']['S']),
                'implant_id': str(implant['implant_id']['S']),
                'implant_partid': fetch_partid(implant['segment1']['S'])}
                
        def fetch_partid(segment1):
            log.info('Fetching partid: %s', segment1)
            if not self.__partid_cache.has_partid(segment1):
                lookup_item = c.get_item(table_name=_LOOKUP_TABLE_NAME,
                    key={'product_code': {'S': segment1}})
                log.info('Got lookup: %s', lookup_item)
                if not lookup_item:
                    return ''
                lookup = lookup_item['Item']
                self.__partid_cache.set_partid(segment1, str(lookup['cs_part_id']['S']))
                log.info('Got partid: %s', str(lookup['cs_part_id']['S']))
            return self.__partid_cache.get_partid(segment1)
        c = self._connection
        implants = Table(_IMPLANTS_TABLE_NAME, connection=c)
        
        matches = implants.query_2(
            index='ImplantID',
            implant_id__eq=implant_id)
            
        return [fetch_implant(str(m['instance_id'])) for m in matches]
        
        
class AsyncSerials(Thread):
    def __init__(self, partid_cache, sleep_duration=1):
        Thread.__init__(self)
        self._implant_ids = Queue()
        self._completed = Queue()
        self._die = False
        self._serials = Serials(partid_cache)
        self._sleep_duration = sleep_duration
        
    def completed(self):
        while not self._completed.empty():
            yield self._completed.get()
        
    def fetch(self, implant_id):
        self._implant_ids.put(implant_id)
        
    def die(self):
        self._die = True
        
    def run(self):
        while not self._die:
            try:
                while not self._implant_ids.empty():
                    self._completed.put(self._serials.fetch(self._implant_ids.get()))
            except Exception, e:
                log.exception(e)
                # Pretend that we got no results.
                # Do NOT retry, that's the responsibility of the application.
                self._completed.put([])
            sleep(self._sleep_duration)
            