## Positional Arguments  

Positional arguments are used to form [arbitrary argument lists](https://docs.python.org/3.6/tutorial/controlflow.html#arbitrary-argument-lists).  

Positional refers to the fact that the relative position, or order, of the arguments is significant when they are stored in their corresponding tuple.  

Positional arguments are optional.   

Positional arguments in Python are similar to [Javascript's Arguments object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments).  

"positional arguments precede keyword arguments and ** unpacking; * unpacking precedes ** unpacking".  

If the form “\*identifier” is present, it is initialized to a tuple receiving any excess positional parameters, defaulting to the empty tuple.  
Parameters after “\*” or “\*identifier” are keyword-only parameters and may only be passed used keyword arguments.  

The * operator instructs Python to pass argument inputs as positional arguments.  

Functions can accept a variable number of positional arguments by using \*args in the def statement.  

- https://docs.python.org/3.6/tutorial/controlflow.html#arbitrary-argument-lists
- https://docs.python.org/3/glossary.html#term-argument
- https://docs.python.org/3/reference/expressions.html#grammar-token-positional_arguments
- https://www.python.org/dev/peps/pep-0362/
- https://www.python.org/dev/peps/pep-0448/
- https://docs.python.org/3/reference/expressions.html#calls
- https://docs.python.org/3/reference/compound_stmts.html#function-definitions
