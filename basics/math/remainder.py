import unittest

"""
Title:

    Remainder using the % (modulo) operator.

Description/Explanation/Lesson:

    The % (modulo) operator yields the remainder from the division of the first argument by the second.
        https://docs.python.org/3/library/operator.html#operator.mod
        https://docs.python.org/3.6/reference/expressions.html#index-59
        https://docs.python.org/3/library/operator.html#mapping-operators-to-functions
        https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

    >>> 3 % 2
    1
    The modulo operator always yields a result with the same sign as its second operand (or zero).
    >>> 3 % 2.0
    1.0

    A simple way to determine if a number is odd or even is to check the remainder when that number is divided by 2.
    For odd numbers, the remainder is 1:
    >>> 3 % 2
    1
    For even numbers, the remainder is 0:
    >>> 4 % 2
    0


Code Prompt/Challenge:

    Set the variable remainder equal to the remainder of 11 divided by 3 using the modulo (%) operator.

Pre-defined Code:

    remainder = "Solution goes here"

Solution:

    remainder = 11 % 3

Tests

    self.assertIsInstance(remainder, int)
    self.assertEqual(remainder, 2)

"""

remainder = 11 % 3

class UnitTests(unittest.TestCase):
    def test_main(self):
        self.assertIsInstance(remainder, int)
        self.assertEqual(remainder, 2)

if __name__=="__main__":
    unittest.main()
