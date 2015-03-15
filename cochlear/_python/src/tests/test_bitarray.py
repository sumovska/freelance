import unittest
from mybitarray import bitarray

class Test_bitarray(unittest.TestCase):
    def test_tobytes_(self):
        self._do_tobytes('', '', '')
        
    def test_tobytes_1(self):
        self._do_tobytes('\x01', '\x80', '1')

    def test_tobytes_0(self):
        self._do_tobytes('\x00', '\x00', '0')

    def test_tobytes_11111111(self):
        self._do_tobytes('\xff', '\xff', '11111111')
        
    def test_tobytes_00000000(self):
        self._do_tobytes('\x00', '\x00', '00000000')

    def test_tobytes_01010101(self):
        self._do_tobytes('\xaa', 'U', '01010101')
       
    def test_tobytes_00001111(self):
        self._do_tobytes('\xf0', '\x0f', '00001111')

    def _do_tobytes(self, expected_little, expected_big, input):
        actual_little = bitarray(input, endian='little').tobytes()
        actual_big = bitarray(input, endian='big').tobytes()
        self.assertEquals((expected_little, expected_big, input), (actual_little, actual_big, input))

    def test_frombytes_(self):
        self._do_frombytes('', '', '')
        
    def test_frombytes_80(self):
        self._do_frombytes('\x80', '\x80', '\x80')

    def test_frombytes_01(self):
        self._do_frombytes('\x01', '\x01', '\x01')

    def _do_frombytes(self, expected_little, expected_big, input):
        a = bitarray(endian='little')
        a.frombytes(input)
        actual_little = a.tobytes()
        a = bitarray(endian='big')
        a.frombytes(input)
        actual_big = a.tobytes()
        
        self.assertEquals((expected_little, expected_big, input), (actual_little, actual_big, input))
        
    def test_slices_little(self):
        a = bitarray('11110000', endian='little')
        expected = ('\x0f', '\x00')
        actual = a[:4].tobytes(), a[4:].tobytes()
        self.assertEquals(expected, actual)

    def test_slices_big(self):
        a = bitarray('11110000', endian='big')
        expected = ('\x00', '\x0f')
        actual = a[:4].tobytes(), a[4:].tobytes()
        self.assertEquals(expected, actual)

    def test_slices_little_2bits(self):
        a = bitarray('10', endian='little')
        expected = ('\x01', '\x00')
        actual = a[:1].tobytes(), a[1:].tobytes()
        self.assertEquals(expected, actual)

    def test_slices_big(self):
        a = bitarray('10', endian='big')
        expected = ('\x80', '\x00')
        actual = a[:1].tobytes(), a[1:].tobytes()
        self.assertEquals(expected, actual)

    def test_bit(self):
        expected = True
        actual = bitarray('10', endian='little')[0]
        self.assertEquals(expected, actual)

if __name__ == '__main__':
    unittest.main()
