import unittest
import float_division_code

class FloatDivisionTests(unittest.TestCase):
    def test_main(self):
        quotient = float_division_code.quotient
        self.assertIsInstance(quotient, float)
        self.assertEqual(quotient, 2.5)
