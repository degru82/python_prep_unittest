import unittest
from sample_func import *


class TestSampleFunc(unittest.TestCase):
    def test_sample_func(self):
        expectedResult = 36
        actualResult = a_func(1, [2, 3, 4], {'a': 5, 'b': 6}, key1=7)
        self.assertEqual(expectedResult, actualResult)


if __name__ == "__main__":
    unittest.main()
