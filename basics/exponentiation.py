import unittest

"""
Title:

    Exponents, aka raising a number to the nth power.

Description/Explanation/Lesson:

    Python uses the double asterisk (**) operator to handle exponentiation.
    The number before the asterisks is the base, and the number after is the exponent.
    Python also lets you use the built-in function pow(x, y), which gives you x to the power of y.
        https://docs.python.org/3/reference/expressions.html#the-power-operator
        https://docs.python.org/3.6/library/operator.html?highlight=operations#operator.pow
        https://docs.python.org/3/library/functions.html#pow
        https://docs.python.org/3/library/operator.html#mapping-operators-to-functions
        https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

    >>> 2 ** 2
    4
    >>> pow(2, 4)
    16

Code Prompt/Challenge:

    In the console, you are given two variables, a and b.
    Using either method described in this lesson, define a variable named power that equals a to the power of b.

Pre-defined Code:

    a = 3
    b = 4

Solution:

    a = 3
    b = 4
    power = pow(a, b)
    --OR--
    power = a ** b

Tests

    self.assertIsInstance(power, int)
    self.assertEqual(power, 81)

"""
a = 3
b = 4
# power = pow(a, b)
power = a ** b


class UnitTests(unittest.TestCase):
    def test_main(self):
        self.assertIsInstance(power, int)
        self.assertEqual(power, 81)

if __name__=="__main__":
    unittest.main()
