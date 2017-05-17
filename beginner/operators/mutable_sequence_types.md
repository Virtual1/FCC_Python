## [Mutable Sequence Types](https://docs.python.org/3.6/library/stdtypes.html#mutable-sequence-types)

The operations in the following table are defined on mutable sequence types. The [collections.abc.MutableSequence](https://docs.python.org/3.6/library/collections.abc.html#collections.abc.MutableSequence) ABC is provided to make it easier to correctly implement these operations on custom sequence types.  

In the table s is an instance of a mutable sequence type, t is any iterable object and x is an arbitrary object that meets any type and value restrictions imposed by s (for example, bytearray only accepts integers that meet the value restriction 0 <= x <= 255).   

*Note About Immutable Sequence Types*  
The only operation that immutable sequence types generally implement that is not also implemented by mutable sequence types is support for the [hash\(\)](https://docs.python.org/3.6/library/functions.html#hash) built-in function.  
&nbsp;

| Operation             | Result                                                                                | Notes |
|-----------------------|---------------------------------------------------------------------------------------|-------|
| s[i] = x              | item i of s is replaced by x                                                          |       |
| s[i:j] = t            | slice of s from i to j is replaced by the contents of the iterable t                  |       |
| del s[i:j]            | same as s[i:j] = []                                                                   |       |
| s[i:j:k] = t          | the elements of s[i:j:k] are replaced by those of t                                   | (1)   |
| del s[i:j:k]          | removes the elements of s[i:j:k] from the list                                        |       |
| s.append(x)           | appends x to the end of the sequence (same as s[len(s):len(s)] = [x])                 |       |
| s.clear()             | removes all items from s (same as del s[:])                                           | (5)   |
| s.copy()              | creates a shallow copy of s (same as s[:])                                            | (5)   |
| s.extend(t) or s += t | extends s with the contents of t (for the most part the same as s[len(s):len(s)] = t) |       |
| s \*= n                | updates s with its contents repeated n times                                          | (6)   |
| s.insert(i, x)        | inserts x into s at the index given by i (same as s[i:i] = [x])                       |       |
| s.pop([i])            | retrieves the item at i and also removes it from s                                    | (2)   |
| s.remove(x)           | remove the first item from s where s[i] == x                                          | (3)   |
| s.reverse()           | reverses the items of s in place                                                      | (4)   |

**Notes:**

1. t must have the same length as the slice it is replacing.  


2. The optional argument i defaults to -1, so that by default the last item is removed and returned.  


3. remove raises ValueError when x is not found in s.


4. The reverse() method modifies the sequence in place for economy of space when reversing a large sequence. To remind users that it operates by side effect, it does not return the reversed sequence.


5. New in version 3.3: clear() and copy() methods. clear() and copy() are included for consistency with the interfaces of mutable containers that don’t support slicing operations (such as dict and set)


6. The value n is an integer, or an object implementing __index__(). Zero and negative values of n clear the sequence. Items in the sequence are not copied; they are referenced multiple times, as explained for s * n under [Common Sequence Operations](https://docs.python.org/3.6/library/stdtypes.html#common-sequence-operations).  
