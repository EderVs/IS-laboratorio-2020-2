"""Contains a decorator that logs after and before function execution"""


def inspect(decorated_function):
    """Decorator that logs something after and before function execution"""
    def wrapper(*args, **kwargs):
        """Wrapper function that adds functionality to decorated function"""
        print('Before function')
        value = decorated_function(*args, **kwargs)
        print('After function')
        return value
    return wrapper


@inspect
def example_function(a, b, c="c"):
    """An example function for decorator testing"""
    print(a)
    print(b)
    print(c)


if __name__ == "__main__":
    example_function(1, 2, 3)
