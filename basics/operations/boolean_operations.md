## [Boolean Operations](https://docs.python.org/3.6/library/stdtypes.html#boolean-operations-and-or-not)  

These are the Boolean operations, ordered by ascending priority (top has lowest priority):  

| Operation | Result                               | Notes |
|-----------|--------------------------------------|-------|
| x or y    | if x is false, then y, else x        | (1)   |
| x and y   | if x is false, then x, else y        | (2)   |
| not x     | if x is false, then True, else False | (3)   |

**Notes:**

1. This is a short-circuit operator, so it only evaluates the second argument if the first one is false.  


2. This is a short-circuit operator, so it only evaluates the second argument if the first one is true.  


3. The not operator has a lower priority than non-Boolean operators, so not a == b is interpreted as not (a == b), and a == not b is a syntax error.
