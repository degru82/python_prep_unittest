import unittest
from unit_decor import *


def dum_func(a, b):
    return a+b


class TestUnitDecor(unittest.TestCase):

    def test_get_param_list_in_string(self):
        expectedResult = "(1, [2, 3, 4], {'a': 5, 'b': 6}, key1=7)"
        actualResult = \
            get_param_list_in_string(1, [2, 3, 4], {'a': 5, 'b': 6}, key1=7)
        self.assertEqual(expectedResult, actualResult)

        expectedResult = "()"
        actualResult = get_param_list_in_string()
        self.assertEqual(expectedResult, actualResult)

    def test_unit_decor(self):
        pass


if __name__ == "__main__":
    unittest.main()
