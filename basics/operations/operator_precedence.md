## Operator Precedence / Order of Operations  
### From the [Python Documentation](https://docs.python.org/3/reference/expressions.html#operator-precedence)  
The following table summarizes the operator precedence in Python, top to bottom, from lowest precedence (least binding) to highest precedence (most binding).

**Note**  
Some of the terms below, such as lambdas and bitwise operations, have not been covered yet.  
If you see an unfamiliar term, worry not young padawan. For reference only, this chart is.

| Operator                                                              | Description                                                             |
|-----------------------------------------------------------------------|-------------------------------------------------------------------------|
| lambda                                                                | Lambda expression                                                       |
| if – else                                                             | Conditional expression                                                  |
| or                                                                    | Boolean OR                                                              |
| and                                                                   | Boolean AND                                                             |
| not x                                                                 | Boolean NOT                                                             |
| in, not in, is, is not, <, <=, >, >=, !=, ==                          | Comparisons, including membership tests and identity tests              |
| |                                                                     | Bitwise OR                                                              |
| ^                                                                     | Bitwise XOR                                                             |
| &                                                                     | Bitwise AND                                                             |
| <<, >>                                                                | Shifts                                                                  |
| +, -                                                                  | Addition and subtraction                                                |
| *, @, /, //, %                                                        | Multiplication, matrix multiplication division, remainder [5]           |
| +x, -x, ~x                                                            | Positive, negative, bitwise NOT                                         |
| **                                                                    | Exponentiation [6]                                                      |
| await x                                                               | Await expression                                                        |
| x[index], x[index:index], x(arguments...), x.attribute                | Subscription, slicing, call, attribute reference                        |
| (expressions...), [expressions...], {key: value...}, {expressions...} | Binding or tuple display, list display, dictionary display, set display |


[5]	The % operator is also used for string formatting; the same precedence applies.  
[6]	The power operator ** binds less tightly than an arithmetic or bitwise unary operator on its right, that is, 2**-1 is 0.5.
