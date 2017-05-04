import unittest

"""
Title:

    Compute quotient and remainder using the divmod function.

Description/Explanation/Lesson:

    Divmod takes two (non complex) numbers as arguments and returns a pair of numbers consisting of their quotient and remainder when using integer division.
    For integers, the result is the same as (a // b, a % b).
        https://docs.python.org/3/library/functions.html#divmod
        https://docs.python.org/3.6/reference/expressions.html#index-59
        https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

    >>> divmod(1, 1)
    (1, 0)
    >>> divmod(3, 2)
    (1, 1)

Code Prompt/Challenge:

    In this exercise, variables a and b are defined for you.
    Define a variable named result that calls the divmod function on variables a and b (in that order).

Pre-defined Code:

    a = 11
    b = 3

Solution:

    a = 11
    b = 3
    result = divmod(a, b)

Tests

    self.assertIsInstance(result, tuple)
    self.assertEqual(result, (3, 2))

"""

a = 11
b = 3
result = divmod(a, b)

class UnitTests(unittest.TestCase):
    def test_main(self):
        self.assertIsInstance(result, tuple)
        self.assertEqual(result, (3, 2))

if __name__=="__main__":
    unittest.main()
