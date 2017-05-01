import unittest
"""

Title:

    Subtract two numbers with Python.

Description/Explanation/Lesson:

    In Python, an integer (int) is one of 3 distinct numeric types.
        https://docs.python.org/3.6/library/stdtypes.html#numeric-types-int-float-complex
    In this exercise, you will subtract two integers using the minus (-) operator.
        https://docs.python.org/3.6/library/operator.html#operator.sub

Code Prompt/Challenge:

    Change the 0 so that total will equal 10.

Pre-defined Code:

    total = 20 - 0

Solution:

    total = 20 - 10

Tests:

    self.assertIsInstance(total, int)
    self.assertEqual(total, 10)

"""

total = 20 - 10

class UnitTests(unittest.TestCase):
    def test_main(self):
        self.assertIsInstance(total, int)
        self.assertEqual(total, 10)

if __name__ == '__main__':
    unittest.main()
