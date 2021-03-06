## [Common Sequence Operations](https://docs.python.org/3.6/library/stdtypes.html#common-sequence-operations)

There are three basic sequence types: lists, tuples, and range objects. Additional sequence types tailored for processing of binary data and text strings are described in dedicated sections.

The operations in the following table are supported by most sequence types, both mutable and immutable. The [collections.abc.Sequence](https://docs.python.org/3.6/library/collections.abc.html#collections.abc.Sequence) ABC is provided to make it easier to correctly implement these operations on custom sequence types.  

This table lists the sequence operations sorted in ascending priority. In the table, s and t are sequences of the same type, n, i, j and k are integers and x is an arbitrary object that meets any type and value restrictions imposed by s.  

The in and not in operations have the same priorities as the comparison operations. The + (concatenation) and * (repetition) operations have the same priority as the corresponding numeric operations.  

| Operation            | Result                                                                           | Notes  |
|----------------------|----------------------------------------------------------------------------------|--------|
| x in s               | True if an item of s is equal to x, else False                                   | (1)    |
| x not in s           | False if an item of s is equal to x, else True                                   | (1)    |
| s + t                | the concatenation of s and t                                                     | (6)(7) |
| s * n or n * s       | equivalent to adding s to itself n times                                         | (2)(7) |
| s[i]                 | ith item of s, origin 0                                                          | (3)    |
| s[i:j]               | slice of s from i to j                                                           | (3)(4) |
| s[i:j:k]             | slice of s from i to j with step k                                               | (3)(5) |
| len(s)               | length of s                                                                      |        |
| min(s)               | smallest item of s                                                               |        |
| max(s)               | largest item of s                                                                |        |
| s.index(x[, i[, j]]) | index of the first occurrence of x in s (at or after index i and before index j) | (8)    |
| s.count(x)           | total number of occurrences of x in s|        |

Sequences of the same type also support comparisons. In particular, tuples and lists are compared lexicographically by comparing corresponding elements. This means that to compare equally, every element must compare equally and the two sequences must be of the same type and have the same length. For full details see [Comparisons](https://docs.python.org/3.6/reference/expressions.html#comparisons) in the language reference.

**Notes:**  

1. While the in and not in operations are used only for simple containment testing in the general case, some specialized sequences (such as str, bytes and bytearray) also use them for subsequence testing:
```
>>> "gg" in "eggs"
True
```  


2. Values of n less than 0 are treated as 0 (which yields an empty sequence of the same type as s). Note that items in the sequence s are not copied; they are referenced multiple times. This often haunts new Python programmers. Here is an example:
```
>>> lists = [[]] * 3
>>> lists
[[], [], []]
>>> lists[0].append(3)
>>> lists
[[3], [3], [3]]
```

- What has happened is that [[]] is a one-element list containing an empty list, so all three elements of [[]] * 3 are references to this single empty list. Modifying any of the elements of lists modifies this single list. You can create a list of different lists this way:
```
>>> lists = [[] for i in range(3)]
>>> lists[0].append(3)
>>> lists[1].append(5)
>>> lists[2].append(7)
>>> lists
[[3], [5], [7]]
```  

- Further explanation is available in the FAQ entry [How do I create a multidimensional list?](https://docs.python.org/3.6/faq/programming.html#faq-multidimensional-list).

3. If i or j is negative, the index is relative to the end of sequence s: len(s) + i or len(s) + j is substituted. But note that -0 is still 0.


4. The slice of s from i to j is defined as the sequence of items with index k such that i <= k < j. If i or j is greater than len(s), use len(s). If i is omitted or None, use 0. If j is omitted or None, use len(s). If i is greater than or equal to j, then the slice is empty.


5. The slice of s from i to j with step k is defined as the sequence of items with index x = i + n\*k such that 0 <= n < (j-i)/k. In other words, the indices are i, i+k, i+2\*k, i+3\*k and so on, stopping when j is reached (but never including j). When k is positive, i and j are reduced to len(s) if they are greater. When k is negative, i and j are reduced to len(s) - 1 if they are greater. If i or j are omitted or None, they become “end” values (which end depends on the sign of k). Note, k cannot be zero. If k is None, it is treated like 1.


6. Concatenating immutable sequences always results in a new object. This means that building up a sequence by repeated concatenation will have a quadratic runtime cost in the total sequence length. To get a linear runtime cost, you must switch to one of the alternatives below:  

	- if concatenating str objects, you can build a list and use str.join() at the end or else write to an io.StringIO instance and retrieve its value when complete  
	- if concatenating bytes objects, you can similarly use bytes.join() or io.BytesIO, or you can do in-place concatenation with a bytearray object. bytearray objects are mutable and have an efficient overallocation mechanism  
	- if concatenating tuple objects, extend a list instead  
	- for other types, investigate the relevant class documentation   

7. Some sequence types (such as range) only support item sequences that follow specific patterns, and hence don’t support sequence concatenation or repetition.


8. index raises ValueError when x is not found in s. When supported, the additional arguments to the index method allow efficient searching of subsections of the sequence. Passing the extra arguments is roughly equivalent to using s[i:j].index(x), only without copying any data and with the returned index being relative to the start of the sequence rather than the start of the slice.
