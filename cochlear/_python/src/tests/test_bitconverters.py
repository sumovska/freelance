from unittest import TestCase
import bitconverters
import math


class test_implant_id(TestCase):

    def test_simple_4(self):
        expected = '1234'
        raw = '\x12\x34\xff'
        actual = bitconverters.implant_id(raw)
        self.assertEqual(expected, actual)

    def test_simple_6(self):
        expected = '234567'
        raw = '\x23\x45\x67'
        actual = bitconverters.implant_id(raw)
        self.assertEqual(expected, actual)

    def test_no_id(self):
        expected = 'No ID'
        raw = '\xff\xff\xff'
        actual = bitconverters.implant_id(raw)
        self.assertEqual(expected, actual)


class test_doubletostr(TestCase):

    def test_nan_str(self):
        ds = bitconverters.doubletostr(float('NaN'))
        self.assertEquals('NaN', str(ds))

    def test_nan_float(self):
        ds = bitconverters.doubletostr(float('NaN'))
        self.assertTrue(math.isnan(float(ds)))
