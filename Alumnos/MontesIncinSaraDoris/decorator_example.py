def my_decorator(function):
    def aux(*args):
        print("Before function")
        function(*args)
        print("After function")
    return aux
    
@my_decorator
def example_function(a, b, c="c"):
    print(a)
    print(b)
    print(c)
    
example_function(1,2,3)
