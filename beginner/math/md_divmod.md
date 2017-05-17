__Title:__  
Compute quotient and remainder using the divmod() function.

__Description/Explanation/Lesson:__

Divmod takes two (non complex) numbers as arguments and returns a pair of numbers consisting of their quotient and remainder when using integer division.  
For integers, the result is the same as (a // b, a % b).
- https://docs.python.org/3/library/functions.html#divmod
- https://forum.freecodecamp.com/t/python-function-divmod/75415
- https://docs.python.org/3.6/reference/expressions.html#index-59
- https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
```
>>> divmod(1, 1)
(1, 0)
>>> divmod(3, 2)
(1, 1)
```

__Code Prompt/Challenge:__

In this exercise, variables a and b are defined for you.
Define a variable named result that calls the divmod function on variables a and b (in that order).

__Pre-defined Code:__
```
a = 11
b = 3
```

__Solution:__
```
a = 11
b = 3
result = divmod(a, b)
```

__Tests:__
```
class UnitTests(unittest.TestCase):
    def test_main(self):
        self.assertIsInstance(result, tuple)
        self.assertEqual(result, (3, 2))
```
