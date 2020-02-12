def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function")
        func(*args, **kwargs)
        print("After function")
    return wrapper     

@my_decorator
def first_function(a,b,c):
    print(a)
    print(b)
    print(c)
first_function(1,2,3)