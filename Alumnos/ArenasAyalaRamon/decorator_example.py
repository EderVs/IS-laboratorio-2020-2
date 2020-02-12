def my_decorator(f):
    def function(*args,**kwargs):
        print("Before function")
        #print (f(*args, **kwargs))
        f(*args, **kwargs)
        print("After function")
    return function

@my_decorator
def suma(a=2,b=3):
    res= a + b
    return(res)

@my_decorator
def example_function(a,b,c='c'):
    print(a)
    print(b)
    print(c)

suma(4,6)
suma()

example_function('a','b')