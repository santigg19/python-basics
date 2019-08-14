import unittest
from roman_numbers import roman_to_decimal

class TestTomanNumbers(unittest.TestCase):

    def test_roman_I_to_decimal(self):
        decimal_number = roman_to_decimal ('I')
        self.assertEqual(decimal_number)


if __name__ == '__main__':
    unittest.__main__()
