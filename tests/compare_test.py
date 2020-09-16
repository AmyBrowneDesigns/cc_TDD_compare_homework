import unittest

from src.compare import compare
from src.compare import compare

class TestCompare(unittest.TestCase):

    def test_compare_3_1_returns_3_is_greater_than_1(self):
        self.assertEqual("3 is greater than 1", compare(3, 1))

    def test_compare_3_5_returns_3_is_less_than_5(self):
        self.assertEqual("3 is less than 5", compare(3, 5))

    def test_compare_10_10returns_10__10(self):
        self.assertEqual("10 is equal to 10", compare(10, 10))
    # return the string "first_number is less than second_number" if the first number is less than the second (e.g. compare(3, 5) => "3 is less than 5")

    # return the string "both numbers are equal" if the two numbers are equal(e.g. compare(10, 10) == "both numbers are equal")