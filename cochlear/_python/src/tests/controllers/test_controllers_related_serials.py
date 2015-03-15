"""
Contains unit tests concerned with "implant serial numbers" on the user interface, and how those flow through the application controllers.
"""

from unittest import TestCase
from engine import SerialsController, DeviceManagerController
from database import MagicDatabase
from serials import AsyncSerials
from devicedetector import DeviceManager
from mock import call, Mock, MagicMock, patch

class WhenLogsAreDownloadedSerialsShouldBeRequested(TestCase):
    @patch('analyzer.LogAnalyzer')
    def testWhenLogsAreAvaiable(self, LogAnalyzer):
        deviceManager = Mock(DeviceManager)
        status_listener = MagicMock()
        on_error = MagicMock()
        save_log = MagicMock()
        
        dmc = DeviceManagerController(deviceManager, status_listener, on_error, save_log)
        
        deviceManager.stuck = False
        deviceManager.logs = MagicMock()
        deviceManager.last_percentage = 100
        deviceManager.has_logs.return_value = True
        LogAnalyzer.return_value.implants.return_value = [['123456', 'some rtc']]
        
        dmc.poll()
        
        expected = 1
        self.assertEquals(expected, len(save_log.mock_calls), on_error.mock_calls)
        
    
class WhenSerialsAreDiscoveredViewShouldBeUpdated(TestCase):
    def setUp(self):
        self._data = Mock(MagicDatabase)
        self._serials = Mock(AsyncSerials)
        self._refresh = MagicMock()
        self._controller = SerialsController(self._data, self._serials, self._refresh)
        
    def test_on_new_serial_updates_database(self):
        self._serials.completed.return_value = [[{'implant_serial':'sn', 'implant_partid': 'ti', 'implant_id': '123456'}]]
        self._controller.new_implant_id('123456')
        self._controller.poll()
        
        expected = [call.add_implant_details('123456', ['sn'], ['ti'])]
        actual = self._data.mock_calls
        
        self.assertEquals(expected, actual)
        
    def test_on_new_serial_updates_view(self):
        self._serials.completed.return_value = [[{'implant_serial':'sn', 'implant_partid': 'ti', 'implant_id': '123456'}]]
        self._controller.new_implant_id('123456')
        self._controller.poll()
        
        expected = [call()]
        actual = self._refresh.mock_calls
        
        self.assertEquals(expected, actual)
        
    def test_does_not_update_view_if_no_serials_updated(self):
        self._serials.completed.return_value = []
        self._data.get_sessions.return_value = []
        self._controller.new_implant_id('123456')
        self._controller.poll()
        
        expected = []
        actual = self._refresh.mock_calls
        
        self.assertEquals(expected, actual)
    
    @patch('time.time')
    def test_should_update_first_time(self, time):
        session = Mock()
        session.implant_id = '1234'
        session.implant_serial_options = []
        
        self._serials.completed.return_value = []
        self._data.get_sessions.return_value = [session]
        time.return_value = 1234567
        self._controller.poll()
        
        actual = [self._data.mock_calls, self._serials.mock_calls, self._refresh.mock_calls]
        expected = [[call.get_sessions('cr220_view')],
            [call.completed(), call.fetch('1234')],
            []] # refresh should only be called if there is NEW data, see 'test_on_new_serial_updates_view'
        
        self.assertEquals(expected, actual)
    
    @patch('time.time')
    def test_should_not_update_again_until_timeout(self, time):
        self._serials.completed.return_value = []
        self._data.get_sessions.return_value = []
        time.return_value = 1234567
        self._controller.poll()
        time.return_value = 1234567+1
        self._controller.poll()
        time.return_value = 1234567+1
        self._controller.poll()
        
        actual = [self._data.mock_calls, self._serials.mock_calls, self._refresh.mock_calls]
        expected = [[call.get_sessions('cr220_view')], # Only updated the first time.
            [call.completed(), call.completed(), call.completed()], # Three polls.
            []] # refresh should only be called if there is NEW data, see 'test_on_new_serial_updates_view'
        
        self.assertEquals(expected, actual)
        
    @patch('time.time')
    def test_should_update_serials_periodically(self, time):
        self._serials.completed.return_value = []
        self._data.get_sessions.return_value = []
        time.return_value = 1234567
        self._controller.poll()
        time.return_value = 1234567+60*5+1
        self._controller.poll()
        
        actual = [self._data.mock_calls, self._serials.mock_calls, self._refresh.mock_calls]
        expected = [[call.get_sessions('cr220_view'), call.get_sessions('cr220_view')], # Updated a second time
            [call.completed(), call.completed()], # Two polls.
            []] # refresh should only be called if there is NEW data, see 'test_on_new_serial_updates_view'
        
        self.assertEquals(expected, actual)