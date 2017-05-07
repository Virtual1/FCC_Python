import unittest

"""
Title:

    Finding the maximum value using the max() function.

Description/Explanation/Lesson:

    The function max() returns the largest item in an iterable (like a list or string), or the largest of two or more arguments.
    While giving an iterable as an argument we must make sure that all of the elements in the iterable are of the same type.
    If the iterable is empty and default is not provided, a ValueError is raised.
        https://docs.python.org/3/library/functions.html#max
        https://forum.freecodecamp.com/t/python-max-function/19205

    >>> max(1,2,3,4)
    4
    >>> list1 = ['a', 'e', 'i', 'o', 'u']
    >>> max(list1)
    'u'
    >>> string1 = "largest"
    >>> max(string1)
    't'


Code Prompt/Challenge:

    The starter code has a list of numbers named, well, numbers.
    The variable highest is initialized to numbers.
    Make the value of highest equal the largest number in numbers.

Pre-defined Code:

    numbers = [8, 2, 4, 3, 6, 5, 9, 1]
    highest = numbers

Solution:

    numbers = [8, 2, 4, 3, 6, 5, 9, 1]
    highest = max(numbers)

Tests

    self.assertIsInstance(highest, int)
    self.assertEqual(highest, 9)

"""

numbers = [8, 2, 4, 3, 6, 5, 9, 1]
highest = max(numbers)

class UnitTests(unittest.TestCase):
    def test_main(self):
        self.assertIsInstance(highest, int)
        self.assertEqual(highest, 9)

if __name__=="__main__":
    unittest.main()
