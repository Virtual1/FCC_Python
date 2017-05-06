__Title:__  Python Float Division

__Description/Explanation/Lesson:__

Python 3 distinguishes between integer (floor) division and float (true) division.  
Python uses a single forward slash (/) operator for float division.  
When using float division, even if the quotient (result) is a whole number like 1 or 2, a floating point number will be returned instead of an int.  
- https://docs.python.org/3/library/operator.html#operator.truediv
- https://docs.python.org/3/library/operator.html#mapping-operators-to-functions
- https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
```
>>> 1 / 1
1.0
>>> 3 / 2
1.5
```

__Code Prompt/Challenge:__

When you run the existing code, the variable named quotient will have a value of 1.0.  
Change the the second number (the denominator) so that quotient has a value of 2.5.

__Pre-defined Code:__
```
quotient = 5 / 5
```

__Solution:__
```
quotient = 5 / 2
```

__Tests:__
```
class UnitTests(unittest.TestCase):
    def test_main(self):
        self.assertIsInstance(quotient, float)
        self.assertEqual(quotient, 2.5)
```
