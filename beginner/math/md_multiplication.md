__Title:__ Python Multiplication

__Description/Explanation/Lesson:__

Python uses the asterisk (\*) operator for multiplication.
- https://docs.python.org/3/library/operator.html#operator.mul
- https://docs.python.org/3/library/operator.html#mapping-operators-to-functions
- https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
```
>>> 3 * 3
9
```

__Code Prompt/Challenge:__

Change the 0 so that product will equal 80.

__Pre-defined Code:__
```
product = 8 * 0
```

__Solution:__
```
product = 8 * 10
```

__Tests:__
```
class UnitTests(unittest.TestCase):
    def test_main(self):
        self.assertIsInstance(product, int)
        self.assertEqual(product, 80)
```
