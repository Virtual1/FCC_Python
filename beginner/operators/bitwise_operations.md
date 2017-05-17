## [Bitwise Operations](https://docs.python.org/3.6/library/stdtypes.html#bitwise-operations-on-integer-types)  

Bitwise operations only make sense for integers. Negative numbers are treated as their 2’s complement value (this assumes that there are enough bits so that no overflow occurs during the operation).

The priorities of the binary bitwise operations are all lower than the numeric operations and higher than the comparisons; the unary operation ~ has the same priority as the other unary numeric operations (+ and -).

This table lists the bitwise operations sorted in ascending priority (top item has least priority):


| Operation | Result                          | Notes  |
|-----------|---------------------------------|--------|
| x \| y    | bitwise or of x and y           |        |
| x ^ y     | bitwise exclusive or of x and y |        |
| x & y     | bitwise and of x and y          |        |
| x << n    | x shifted left by n bits        | (1)(2) |
| x >> n    | x shifted right by n bits       | (1)(3) |
| ~x        | the bits of x inverted          |        |

**Notes:**

1. Negative shift counts are illegal and cause a ValueError to be raised.  


2. A left shift by n bits is equivalent to multiplication by pow(2, n) without overflow check.  


3. A right shift by n bits is equivalent to division by pow(2, n) without overflow check.
