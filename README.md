# Cursed python scripts

## Number substitution

Modifying C struct of `int` class to make Python think that 42 equals 80. See `number_substitution.py`
Originates from some Habr article about internal CPython structure.

## Summator

Not very cursed, but fun. Call pipe for calulating sum of numbers:
```
>>> Summator(5)(10)(-10)(2)
7
```
See `summator.py`

## stdout

It must be a great question for interviewing Python developers:

**Can this line be used to print line in console in Python?**

```
cout << "Hello, world!" << endl;
```

The correct answer is **YES**! See `stdout.py`


## Decorator

`decorator.py` is not cursed nor funny. There is decorator that transform functions into int

It just demonstrates that decorator is just a function with syntax sugar and

```python
@deco
def foo():
  ...
```

equals to

```python
def foo():
  ...

foo = deco(foo)
```
