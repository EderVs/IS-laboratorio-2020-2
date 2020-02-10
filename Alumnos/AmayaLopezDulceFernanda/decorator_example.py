def my_decorator(f):
    def aux(*args, **kwargs):
        print("Before function\n")
        f(*args, **kwargs)
        print("\nAfter function")
    return aux

@my_decorator
def example_function(a, b, c="c"):
    print(a)
    print(b)
    print(c)

example_function(1, 2, c=3)
