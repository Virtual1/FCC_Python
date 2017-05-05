__Title:__ Python integer division.

__Description/Explanation/Lesson:__

Python 3 distinguishes between integer (floor) division and float (true) division.  
Python uses a double forward slash (//) operator for integer division.  
When using integer division, Python will round the quotient down to the nearest whole number.  
- https://docs.python.org/3/library/operator.html#operator.floordiv
- https://docs.python.org/3/library/operator.html#mapping-operators-to-functions
- https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
```
>>> 1 // 1
1
>>> 3 // 2
1
```

__Code Prompt/Challenge:__

When you run the existing code, the variable named quotient will have a value of 1.  
Change the the second number (the denominator) so that quotient has a value of 2.

__Pre-defined Code:__
```
quotient = 5 // 5
```

__Solution:__
```
quotient = 5 // 2
```
__Tests:__
```
class UnitTests(unittest.TestCase):
    def test_main(self):
        self.assertIsInstance(quotient, int)
        self.assertEqual(quotient, 2)
```
