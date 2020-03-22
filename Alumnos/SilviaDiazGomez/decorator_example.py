import functools

def my_decorator(function):
    def wrapper(*args):
        print("Before function")
        function(*args)
        print("After function")
    return wrapper

