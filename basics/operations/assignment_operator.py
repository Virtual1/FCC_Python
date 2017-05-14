# Comment below the following details:
# Title
# Description/Explanation/Lesson
# Code Prompt/Challenge
# Pre-defined Code
# Solution
# Tests

import unittest

"""
Title:

    Python Assignment Operator

Description/Explanation/Lesson:

    In Python the assignment operator is represented by a single equal sign (=).
    The equal sign (=) is used to assign a value on the right of the operator to a variable on the left of the operator, also known as an assignment statement.
        https://docs.python.org/3.6/reference/simple_stmts.html#assignment-statements

    >>> letter = 'a'
    >>> print(letter)
    a
    >>> number = 42
    >>> print(number)
    42
    >>> number = 3.14
    >>> print(number)
    3.14

Code Prompt/Challenge:

    Time to introduce yourself, fledgling Pythonista!
    In the console, create a variable called my_name.
    Assign a string containing your name to the variable my_name.

Pre-defined Code:

    ### Write your code below this line. ###



    ### Write your code above this line. ###

    print("Hello, my name is " + my_name)

Solution:

    my_name = "Any string will pass"

Tests

    self.assertIsInstance(my_name, str)

"""

### Write your code below this line. ###

my_name = "Monty Python"

### Write your code above this line. ###

print("Hello, my name is " + my_name)

class UnitTests(unittest.TestCase):
    def test_main(self):
        self.assertIsInstance(my_name, str)

if __name__=="__main__":
    unittest.main()
