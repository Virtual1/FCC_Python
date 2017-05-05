__Title:__ Python Addition

__Description/Explanation/Lesson:__

In Python, an integer (int) is one of 3 distinct numeric types.  
In this exercise, you will add two integers using the plus (+) operator.
- https://docs.python.org/3.6/library/stdtypes.html#numeric-types-int-float-complex
- https://docs.python.org/3.6/library/operator.html#operator.add
- https://docs.python.org/3/library/operator.html#mapping-operators-to-functions
```
>>> 2 + 2
4
```

__Code Prompt/Challenge:__

Change the 0 so that total will equal 20.

__Pre-defined Code:__
```
total = 10 + 0
```

__Solution:__
```
total = 10 + 10
```

__Tests:__
```
class UnitTests(unittest.TestCase):
    def test_main(self):
        self.assertIsInstance(total, int)
        self.assertEqual(total, 20)
```
