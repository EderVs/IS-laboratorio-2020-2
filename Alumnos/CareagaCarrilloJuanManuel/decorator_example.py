def my_decorator(f):
    def decorated(*args, **kwargs):
        print("Before function")
        f(*args, **kwargs)
        print("After function")
    return decorated

@my_decorator
def example_function(a, b, c="c"):
    print("a")
    print("b")
    print("c")


example_function(1, 2, c=3)

