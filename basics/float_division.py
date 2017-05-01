import unittest

"""
Title:

    Divide two numbers with Python using float division.

Description/Explanation/Lesson:

    Python 3 distinguishes between integer (floor) division and float (true) division.
    Python uses a single forward slash (/) operator for float division.
    When using float division, even if the quotient (result) is a whole number like 1 or 2, a floating point number will be returned instead of an int.
        https://docs.python.org/3/library/operator.html#operator.truediv
        https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Code Prompt/Challenge:

    When you run existing code, the variable named quotient will have a value of 1.0.
    Change the the second number (the denominator) so that quotient will have a value of 2.5.

Pre-defined Code:

    quotient = 5 / 5

Solution:

    quotient = 5 / 2

Tests

    self.assertIsInstance(quotient, float)
    self.assertEqual(quotient, 2.5)

"""

quotient  = 5 / 2

class UnitTests(unittest.TestCase):
    def test_main(self):
        self.assertIsInstance(quotient, float)
        self.assertEqual(quotient, 2.5)

if __name__=="__main__":
    unittest.main()
