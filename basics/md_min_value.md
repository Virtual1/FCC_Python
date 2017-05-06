__Title:__ Python Minimum Value

__Description/Explanation/Lesson:__

The function min() returns the smallest item in an iterable (like a list or string), or the smallest of two or more arguments.  
While giving an iterable as an argument we must make sure that all of the elements in the iterable are of the same type.  
If the iterable is empty and default is not provided, a ValueError is raised.  
- https://docs.python.org/3/library/functions.html#min
- https://forum.freecodecamp.com/t/python-min-function/19204
```
>>> min(1,2,3,4)
1
>>> list1 = ['a', 'e', 'i', 'o', 'u']
>>> min(list1)
'a'
>>> string1 = "smallest"
>>> min(string1)
'a'
```

__Code Prompt/Challenge:__

The starter code has a list of letters named, well, letters.  
The variable lowest is initialized to letters.  
Make the value of lowest equal the 'smallest' (alphabetically first) letter in letters.  

__Pre-defined Code:__
```
letters = ['m','o','n','t','y','p','y','t','h','o','n']
lowest = letters
```

__Solution:__
```
letters = ['m','o','n','t','y','p','y','t','h','o','n']
lowest = min(letters)
```

__Tests:__
```
class UnitTests(unittest.TestCase):
    def test_main(self):
        self.assertIsInstance(lowest, str)
        self.assertEqual(lowest, 'h')
```
