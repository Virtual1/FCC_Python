import unittest
import math

"""
Title:

    Calculate the square root of a number using the math.sqrt() function.

Description/Explanation/Lesson:

    The math.sqrt() function is a part of Python's math module, which is always available but must be imported.
    Math.sqrt(x) returns the square root of x as a floating-point number.
        https://docs.python.org/3/library/math.html
        https://docs.python.org/3.6/library/math.html?highlight=sqrt#math.sqrt

    >>> import math
    >>> math.sqrt(4)
    2.0
    >>> math.sqrt(2)
    1.4142135623730951

Code Prompt/Challenge:

    The variable square_root is defined as the number 81.
    Change square_root so that it equals the square root of 81.
    The math module has been imported for you.

Pre-defined Code:

    import math
    square_root = 81

Solution:

    import math
    square_root = math.sqrt(81)

Tests

    self.assertIsInstance(square_root, float)
    self.assertEqual(square_root, 9.0)

"""

square_root = math.sqrt(81)

class UnitTests(unittest.TestCase):
    def test_main(self):
        self.assertIsInstance(square_root, float)
        self.assertEqual(square_root, 9.0)

if __name__=="__main__":
    unittest.main()
