# For loops

## When it is used?

The `for` loop is used for iterating over a sequence, say, for example, over a list.

Syntax:

```python
for iterating_var in sequence:
    statement(s)
```

It is normally used when you want to execute a block of code a **fixed**, or *known*, number of times. 

## Range function

You can use the built-in function `range()` within a for loop, like this:

```python
for i in range(5):
    print(i)
```

The code above prints the integers from 0 to 4. Note here that the 5 is excluded, meaning that the range function, when called with one argument, generates a series of numbers starting at 0 and including every whole number up to, but not including, the number provided as argument.

There are other variants to the range function:
* `range(start, stop)` -> starts at the number provided as the first arg, all the way up to, but not including, the number provided as the second arg.

* `range(start, stop, step)` -> Similar to the one above, but here, `step` determines the increment between each integer in the sequence.