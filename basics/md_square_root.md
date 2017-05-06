__Title:__ Python Square Root

__Description/Explanation/Lesson:__

The math.sqrt() function is a part of Python's math module, which is always available but must be imported.  
Math.sqrt(x) returns the square root of x as a floating-point number.  
- https://docs.python.org/3/library/math.html
- https://docs.python.org/3.6/library/math.html?highlight=sqrt#math.sqrt
```
>>> import math
>>> math.sqrt(4)
2.0
>>> math.sqrt(2)
1.4142135623730951
```

__Code Prompt/Challenge:__

The variable square_root is defined as the number 81.  
Change square_root so that it equals the square root of 81.  
The math module has been imported for you.  

__Pre-defined Code:__
```
import math
square_root = 81
```

__Solution:___
```
import math
square_root = math.sqrt(81)
```

__Tests:__
```
class UnitTests(unittest.TestCase):
    def test_main(self):
        self.assertIsInstance(square_root, float)
        self.assertEqual(square_root, 9.0)
```
