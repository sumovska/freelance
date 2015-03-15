
from unittest import TestCase
from serials import AsyncSerials
from database import MagicDatabase
from mh_email import MagicHatEmail
from devicedetector import DeviceManager
from magichat import MainApp
from mock import Mock, MagicMock, patch
from engine import ExposedMethods

class NaiveTests(TestCase):
    def setUp(self):
        self._em = ExposedMethods(Mock(AsyncSerials), Mock(MagicDatabase), Mock(MagicHatEmail), Mock(MainApp), Mock(DeviceManager))
        
    @patch('engine.EmailController')
    @patch('engine.SerialsController')
    @patch('engine.DeviceManagerController')
    def testPoll(self, dcm, sc, ec):
        self._em.refresh = MagicMock()
        self._em.poll()
        
        self.assertEquals((1, 1, 1),(
            len(dcm.mock_calls),
            len(sc.mock_calls),
            len(ec.mock_calls)))