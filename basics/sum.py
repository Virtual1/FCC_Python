import unittest

"""
Title:

    Using Python's sum() function.

Description/Explanation/Lesson:

    The function sum(iterable) adds all of the items in a Python iterable (list, tuple, and so on) from left to right and returns the total.
    There is an optional second argument, start, that defaults to 0 and is added to the total.
    The iterable‘s items are normally numbers, and the start value is not allowed to be a string.
        https://docs.python.org/3/library/functions.html#sum

    >>> numbers = [1, 2, 3, 4, 5]
    >>> sum(numbers)
    15
    >>> sum(numbers, 1)
    16
    >>> sum(numbers, 10)
    25

Code Prompt/Challenge:

    There are two lists of numbers.
    Find the sum of all of the items in both lists and assign that value to a variable named total.

Pre-defined Code:

    list1 = [1, 3, 5, 7, 9]
    list2 = [2, 4, 6, 8, 10]

Solution:

    list1 = [1, 3, 5, 7, 9]
    list2 = [2, 4, 6, 8, 10]
    total = sum(list1, sum(list2))

Tests

    self.assertIsInstance(total, int)
    self.assertEqual(total, 55)

"""

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
total = sum(list1, sum(list2))

class UnitTests(unittest.TestCase):
    def test_main(self):
        self.assertIsInstance(total, int)
        self.assertEqual(total, 55)

if __name__=="__main__":
    unittest.main()
