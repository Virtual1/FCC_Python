import unittest
import integer_division_code

class IntegerDivisionTests(unittest.TestCase):
    def test_main(self):
        quotient = integer_division_code.quotient
        self.assertIsInstance(quotient, int)
        self.assertEqual(quotient, 2)
