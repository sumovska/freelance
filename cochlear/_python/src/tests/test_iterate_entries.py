import unittest
import parsers.baselog as parsers

ENTRY_LENGTH = 66
NULL_ENTRY = [0]*ENTRY_LENGTH

class Test_iterate_entries_test(unittest.TestCase):
    def test_empty(self):
        self.assertEquals([], list(parsers.iterate_entries([], ENTRY_LENGTH, 0, 0, 0, False)))

    def test_trivial(self):
        self.assertEquals([
            [1]*ENTRY_LENGTH,
            [2]*ENTRY_LENGTH,
            [3]*ENTRY_LENGTH,
            [4]*ENTRY_LENGTH], list(parsers.iterate_entries(
            [1]*ENTRY_LENGTH +
            [2]*ENTRY_LENGTH +
            [3]*ENTRY_LENGTH +
            [4]*ENTRY_LENGTH, ENTRY_LENGTH, 0, 3, 4, False)))

    def test_loop(self):
        self.assertEquals([
            [1]*ENTRY_LENGTH,
            [2]*ENTRY_LENGTH,
            [3]*ENTRY_LENGTH,
            [4]*ENTRY_LENGTH], list(parsers.iterate_entries(
            [2]*ENTRY_LENGTH +
            [3]*ENTRY_LENGTH +
            [4]*ENTRY_LENGTH +
            [1]*ENTRY_LENGTH, ENTRY_LENGTH, 3, 2, 4, False)))

    def test_overwritten(self):
        self.assertEquals([
            [2]*ENTRY_LENGTH,
            [3]*ENTRY_LENGTH,
            [4]*ENTRY_LENGTH,
            [5]*ENTRY_LENGTH], list(parsers.iterate_entries(
            [2]*ENTRY_LENGTH +
            [3]*ENTRY_LENGTH +
            [4]*ENTRY_LENGTH +
            [5]*ENTRY_LENGTH, ENTRY_LENGTH, 3, 3, 5, True)))
        
    def test_12_of_123(self):
        self.assertEquals([
            [1]*ENTRY_LENGTH,
            [2]*ENTRY_LENGTH], list(parsers.iterate_entries(
            [1]*ENTRY_LENGTH +
            [2]*ENTRY_LENGTH +
            [3]*ENTRY_LENGTH, ENTRY_LENGTH, 0, 1, 2, False)))
    def test_23_of_123(self):
        self.assertEquals([
            [1]*ENTRY_LENGTH,
            [2]*ENTRY_LENGTH], list(parsers.iterate_entries(
            [3]*ENTRY_LENGTH +
            [1]*ENTRY_LENGTH +
            [2]*ENTRY_LENGTH, ENTRY_LENGTH, 1, 2, 2, False)))
    def test_31_of_123(self):
        self.assertEquals([
            [1]*ENTRY_LENGTH,
            [2]*ENTRY_LENGTH], list(parsers.iterate_entries(
            [2]*ENTRY_LENGTH +
            [3]*ENTRY_LENGTH +
            [1]*ENTRY_LENGTH, ENTRY_LENGTH, 2, 0, 2, False)))

if __name__ == '__main__':
    unittest.main()
