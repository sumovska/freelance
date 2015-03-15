from unittest import TestCase
from serials import Serials, AsyncSerials
from mock import Mock, call, patch
from database import MagicDatabase
from time import sleep

class SystemTestsSerials(TestCase):
    maxTime = 2
    def setUp(self):
        self._partids = Mock(MagicDatabase)
        self._serials = Serials(self._partids)
        
    def _perform_test(self):
        implant_id = '0071'
        expected = [{
            'implant_id': '0071',
            'implant_serial': '1020051935646',
            'implant_partid': '7623'}, {
            'implant_id': '0071',
            'implant_serial': '1020050562072',
            'implant_partid': '7623'}, {
            'implant_id': '0071',
            'implant_serial': '1020020721820',
            'implant_partid': '6805'}]
        expected.sort(key=lambda x: x['implant_serial'])
        actual = self._serials.fetch(implant_id)
        actual.sort(key=lambda x: x['implant_serial'])
        
        self.assertEquals(expected, actual)
        
    def testQueryRealDbForValidID_all_in_cache(self):
        
        self._partids.has_partid.return_value = True
        self._partids.get_partid.side_effect=['7623', '7623', '6805']
        self._partids.set_partid.side_effect=Exception()
        
        self._perform_test()
        expected = [
            call.has_partid('Z60353'),
            call.get_partid('Z60353'),
            call.has_partid('Z60353'),
            call.get_partid('Z60353'),
            call.has_partid('Z60132'),
            call.get_partid('Z60132'),
            ]
        self.assertEquals(self._partids.mock_calls, expected)
        
    def testQueryRealDbForValidID_none_in_cache(self):
        
        self._partids.has_partid.side_effect = [False, True, False]
        self._partids.get_partid.side_effect=['7623', '7623', '6805']
        
        self._perform_test()
        expected = [
            call.has_partid('Z60353'),
            call.set_partid('Z60353', '7623'),
            call.get_partid('Z60353'),
            call.has_partid('Z60353'),
            call.get_partid('Z60353'),
            call.has_partid('Z60132'),
            call.set_partid('Z60132', '6805'),
            call.get_partid('Z60132')]
        self.assertEquals(self._partids.mock_calls, expected)
        
    def testQueryRealDBForInvalidPartId(self):
        implant_id = '9963' # This is a CI422 implant that, somehow, does not have a valid part id.
        self._partids.has_partid.return_value = False
        expected = [{'implant_id': implant_id, 'implant_partid': '', 'implant_serial': '1020142026770'}]
        actual = self._serials.fetch(implant_id)
        
        self.assertEquals(expected, actual)
        
    def testQueryRealDbForInvalidID(self):
        implant_id = '2' # Completely invalid: ID's are 4 or 6 digits, so it's impossible for this to match.
        expected = []
        actual = self._serials.fetch(implant_id)
        
        self.assertEquals(expected, actual)
        
        
class AsyncSerialsTest(TestCase):
    @patch('serials.Serials')
    def testSimpleFetch(self, Serials):
        data = Mock(MagicDatabase)
        aserials = AsyncSerials(data, sleep_duration=0.025)
        aserials.start()
        try:
            result = 'The Result of Fetch!'
            Serials.return_value.fetch.return_value = result
            
            aserials.fetch('123456')
            sleep(0.05)
            completed = list(aserials.completed())
            
            self.assertEquals([result], completed)
        finally:
            aserials.die()
            aserials.join()