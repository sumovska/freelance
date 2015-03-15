from unittest import TestCase
from report import Report, ReportException
from mock import Mock, patch
from database import Session, MagicDatabase

class TestReport(TestCase):
    def setUp(self):
        db = Mock(MagicDatabase)
        db.get_names.return_value = []
        self._data = [Session(db, **{
            'name_first':'First Name',
            'name_last':'Last Name',
            'impedances_chart': 'binary .png data for impedances',
            'nrt_profile_chart': 'binary .png data for nrt profile',
            'dob': '1234-12-12',
            'utc_date': '2021-02-03T12:13:15',
            'gender': 'Male',
            'surgery': 'Surgery',
            'surgeon': 'Surgeon',
            'clinic': 'Clinic',
            'serial': '123412'
        }).as_dict()]
        

    def test_init_should_die_if_insufficient_data(self):
        self.assertRaises(ReportException, lambda: Report([{}]))

    def test_init_should_pass_with_good_arguments(self):
        self.assertIsNotNone(Report(self._data))

    @patch('report.JsonEncoder')
    def test_html(self, jsonEncoder):
        self.assertTrue('<html>' in Report(self._data).html())

    @patch('report.JsonEncoder')
    def test_pdf(self, jsonEncoder):
        self.assertTrue('%%EOF' in Report(self._data).pdf())