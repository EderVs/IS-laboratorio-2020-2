
def my_decorator(fun):
    def befoaft(*args,**kwargs):
        print("Before function")
        fun(*args,**kwargs)
        print("After function")
    return befoaft

@my_decorator
def example_function(a,b,c="c"):
    print(a)
    print(b)
    print(c)

example_function(1,2,c=3)