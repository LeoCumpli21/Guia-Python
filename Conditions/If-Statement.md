# Flow control with if

## If statement

The **`if` statement** is used for decision making. When is decision making required? When we want our code to execute something **if** a certain **condition** is satisfied.

The sytax of an if statement is:

```python
if condition:
    statement(s)
```

The **condition** is an expression that evaluates to `True` or `False`. If the condition evaluates to `True`, the indented code block below will be executed. If it evaluates to `False`, the indented code block below won't be executed.

So, the body of the `if` statement is **always** indented.

## If-else statement

Syntax:

```python
if condition:
    statement(s)
else:
    statement(s)
```

Here, if the condition evaluates to `True`, the body of `if` is executed. If it evaluates to `False`, the body of `else` is executed.

## If-elif-else statement

Syntax:

```python
if condition:
    code
elif condition:
    code
else:
    code
```

Notice that now there's another check of some conditon, done by the `elif` statement. You can have as many elif statements as you want inside an `if`. At the end, in case no condition is satisfied, you can add the `else` to execute some code.

## Nested if

A *nested if* is an if statement **inside** antoher if statement.

Syntax:

```python
if condition1:
    if condition2:
        code # this is executed only if the nested if condition evaluates to True
    # nested if ends here
    code # This block corresponds to the outer most if statment
```
