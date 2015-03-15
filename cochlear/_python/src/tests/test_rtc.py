import unittest
from bitconverters import rtc
from mybitarray import bitarray


class test_rtc(unittest.TestCase):
    def test_documented_maximums(self):
        """
        This represents the maximum values allowed by the documentation
        """
        max = bitarray('110111 110111 11101 011101101 111111111111 00'.replace(' ', ''), endian='little')
        expected = 'P1496064DT23H59M59S'
        actual = rtc(max.tobytes())
        self.assertEquals(expected, actual)

    def test_real_maximums(self):
        """
        This represents the maximum values allowed by the implementation
        """
        max = bitarray('111111 111111 11111 111111111 111111111111 00'.replace(' ', ''), endian='little')
        expected = 'P1496209DT31H63M63S'
        actual = rtc(max.tobytes())
        self.assertEquals(expected, actual)

    def test_zeros(self):
        zero= bitarray('000000 000000 00000 000000000 000000000000 00'.replace(' ', ''), endian='little')
        expected = 'P0DT0H0M0S'
        actual = rtc(zero.tobytes())
        self.assertEquals(expected, actual)

    def test_one_day(self):
        raw = '\x16\x07\x04\x00\x00'
        raw = bitarray('011010 001110 00000 010000000 000000000000 00'.replace(' ', ''), endian='little')
        expected = "P1DT0H28M22S"
        actual = rtc(raw.tobytes())
        self.assertEquals(expected, actual)


if __name__ == '__main__':
    unittest.main()
