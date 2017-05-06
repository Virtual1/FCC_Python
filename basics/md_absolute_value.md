__Title:__ Python Absolute Value

__Description/Explanation/Lesson:__  

Absolute value refers to how far a number is from zero.  
If a number is negative, abs() will convert it to positive.  
In abs(x), x may be an integer, float, or complex number.    
- https://docs.python.org/3/library/functions.html#abs
- https://forum.freecodecamp.com/t/python-abs-x-function/19212
- https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
```
>>> abs(2)
2
>>> abs(-2)
2
>>> abs(-2.0)
2.0
```

__Code Prompt/Challenge:__

The variable absolute_value equals -42.  
Change absolute_value so that it equals the absolute value of -42.

__Pre-defined Code:__
```
absolute_value = -42
```
__Solution:__
```
absolute_value = abs(-42)
```
__Tests:__
```
class UnitTests(unittest.TestCase):
    def test_main(self):
        self.assertIsInstance(absolute_value, int)
        self.assertEqual(absolute_value, 42)
```
