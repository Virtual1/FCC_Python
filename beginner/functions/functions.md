## Python Functions  

built-in-functions vs user-defined-functions  
function arguments/ types of arguments   
function docstrings and function design recipe  
return statement (or no return statement)  
calling functions  
variable scope? -- maybe better left to variables section  
anonymous functions? -- maybe better left to intermediate section


- https://docs.python.org/2/tutorial/controlflow.html#defining-functions
- https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions
- https://docs.python.org/3/library/functions.html#built-in-functions
- https://www.tutorialspoint.com/python/python_functions.htm


### [Writing user-defined functions in Python](https://www.codementor.io/python/tutorial/user-defined-functions-in-python-beginners)  
- https://www.codementor.io/python/tutorial/user-defined-functions-in-python-beginners  

These are the basic steps in writing user-defined functions in Python.  
For additional functionalities, we need to incorporate more steps as needed.  

1. Declare the function with the keyword `def` followed by the function name.
2. Write the arguments inside the opening and closing parentheses of the function, and end the declaration with a colon.
3. Add the program statements to be executed.
4. End the function with/without return statement.

```
>>> def say_hello():
...     print("Hello World!")
...
>>> say_hello()
Hello World!
```

```
>>> def say_hello(greeting):
...     print(greeting)
...
>>> say_hello("Hello World!")
Hello World!
```

```
>>> def say_hello(greeting):
...     print(greeting)
...     return True
...
>>> say_hello("Hello World!")
Hello World!
True
```

### Function Design Recipe  
- https://www.ics.uci.edu/~kay/courses/31/design-recipe.html
- [University of Toronto via Coursera](https://d18ky98rnyall9.cloudfront.net/\_96168b6c868aaef1d7f57b6f4a7b0b03_designrecipe.html?Expires=1497052800&Signature=ZM4J6w-E8DdRjSkQz1EMiAYwyf-UuSE-neU0SMPaGXAuOkwOjLlc5AzrqeuT2tpgmnBm~arTZnCBSq9FYmcBfUaF8KrDnsdkmb1nw7gGS1LzJNfaEjfquyW0MSpQYE50cTcYcrM4TnSz0rbqxD7f-PYkp3~CRIZEhR8anCFL6pY_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)
- Practical Programming An Introduction to Computer Science Using Python 3.pdf  3.6 Designing New Functions: A Recipe  
- http://vincenttse.com/design-recipe/
