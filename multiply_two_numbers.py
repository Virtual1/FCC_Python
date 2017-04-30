import unittest

"""
Title:

    Multiply two numbers with Python.

Description/Explanation/Lesson:

    Python uses the asterisk (*) operator for multiplication.
        https://docs.python.org/3/library/operator.html#operator.mul
        https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Code Prompt/Challenge:

    Change the 0 so that product will equal 80.

Pre-defined Code:

    product = 8 * 0

Solution:

    product = 8 * 10

Tests

    self.assertIsInstance(product, int)
    self.assertEqual(product, 80)

"""

product = 8 * 10

class UnitTests(unittest.TestCase):
    def test_main(self):
        self.assertIsInstance(product, int)
        self.assertEqual(product, 80)

if __name__=="__main__":
    unittest.main()
