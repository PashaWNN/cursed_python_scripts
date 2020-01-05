def my_decorator(f):
    return 42


@my_decorator
def foo(a, b):
    return a + b


print(type(foo))  # Prints "<type 'int'>"

print(foo)  # Prints "42"

foo()  # Raises exception
