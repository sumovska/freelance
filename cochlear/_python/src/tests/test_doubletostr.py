import unittest
from bitconverters import doubletostr

class Test_doubletostr(unittest.TestCase):
    """
    The careful reviewer will note that these are an
    incorrect number of significant decimals.

    This needs to mimic CDI
    """
    def test_1_21183205_to_6sf(self):
        input = 1.21183205
        expected = '1.211832'
        actual = str(doubletostr(input, 6))
        self.assertEquals(expected, actual)  

    def test_0_958255_to_5sf(self):
        input = 0.9582541234
        expected = '0.958254'
        actual = str(doubletostr(input, 5))
        self.assertEquals(expected, actual)

    def test_0_702754_to_5sf(self):
        input = 0.7027541234
        expected = '0.702754'
        actual = str(doubletostr(input, 5))
        self.assertEquals(expected, actual)

if __name__ == '__main__':
    unittest.main()
