__Title:__ Python Rounding

__Description/Explanation/Lesson:__

The function round(number, n-digits) returns a given number rounded to n-digits precision after the decimal point.  
If n-digits is omitted or is None, it returns the nearest integer to its input.  
The return value is an integer if called with one argument, otherwise it is of the same type as the given number.  
- https://docs.python.org/3/library/functions.html#round
```
>>> round(5)
5
>>> round(5.5)
6
>>> round(5.555, 1)
5.6
```

__Code Prompt/Challenge:__

The variable longer_pi has too many digits after the decimal place.  
Create a variable named shorter_pi that we can use instead.  
Use the round() function to display just the first 2 digits after the decimal point, and assign that value to shorter_pi.  

__Pre-defined Code:__
```
longer_pi = 3.14159265358979323846
```

__Solution:__
```
longer_pi = 3.14159265358979323846
shorter_pi = round(longer_pi, 2)
```

__Tests:__
```
class UnitTests(unittest.TestCase):
    def test_main(self):
        self.assertIsInstance(shorter_pi, float)
        self.assertEqual(shorter_pi, 3.14)
```
