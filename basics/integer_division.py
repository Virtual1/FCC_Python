import unittest

"""
Title:

    Divide two numbers with Python using integer division.

Description/Explanation/Lesson:

    Python 3 distinguishes between integer (floor) division and float (true) division.
    Python uses a double forward slash (//) operator for integer division.
    When using integer division, Python will round the quotient down to the nearest whole number.
        https://docs.python.org/3/library/operator.html#operator.floordiv
        https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Code Prompt/Challenge:

    When you run existing code, the variable named quotient will have a value of 1.
    Change the the second number (the denominator) so that quotient will have a value of 2.

Pre-defined Code:

    quotient = 5 // 5

Solution:

    quotient = 5 // 2

Tests

    self.assertIsInstance(quotient, int)
    self.assertEqual(quotient, 2)

"""

quotient  = 5 // 2

class UnitTests(unittest.TestCase):
    def test_main(self):
        self.assertIsInstance(quotient, int)
        self.assertEqual(quotient, 2)

if __name__=="__main__":
    unittest.main()
