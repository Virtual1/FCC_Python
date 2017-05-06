__Title:__ Python Subtraction

__Description/Explanation/Lesson:__

In Python, an integer (int) is one of 3 distinct numeric types.  
In this exercise, you will subtract two integers using the minus (-) operator.
- https://docs.python.org/3.6/library/stdtypes.html#numeric-types-int-float-complex
- https://docs.python.org/3.6/library/operator.html#operator.sub
- https://docs.python.org/3/library/operator.html#mapping-operators-to-functions
```
>>> 2 - 1
1
```

__Code Prompt/Challenge:__

Change the 0 so that total will equal 10.

__Pre-defined Code:__
```
total = 20 - 0
```

__Solution:__
```
total = 20 - 10
```

__Tests:__
```
class UnitTests(unittest.TestCase):
    def test_main(self):
        self.assertIsInstance(total, int)
        self.assertEqual(total, 10)
```
