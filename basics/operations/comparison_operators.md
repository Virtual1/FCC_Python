## [Comparison Operators](https://docs.python.org/3.6/library/stdtypes.html#comparisons)  

There are eight comparison operations in Python.  
All of these operators return a boolean true or false value.  
They all have the same priority (which is higher than that of the Boolean operations).  
Comparisons can be chained arbitrarily; for example, x < y <= z is equivalent to x < y and y <= z, except that y is evaluated only once (but in both cases z is not evaluated at all when x < y is found to be false).

This table summarizes the comparison operations:

| Operation | Meaning                 |
|-----------|-------------------------|
| <         | strictly less than      |
| <=        | less than or equal      |
| >         | strictly greater than   |
| >=        | greater than or equal   |
| ==        | equal                   |
| !=        | not equal               |
| is        | object identity         |
| is not    | negated object identity |

Objects of different types, except different numeric types, never compare equally.  
Furthermore, some types (for example, function objects) support only a degenerate notion of comparison where any two objects of that type are unequal.  
The <, <=, > and >= operators will raise a TypeError exception when comparing a complex number with another built-in numeric type, when the objects are of different types that cannot be compared, or in other cases where there is no defined ordering.
