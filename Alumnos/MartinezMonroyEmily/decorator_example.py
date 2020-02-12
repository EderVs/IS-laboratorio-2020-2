"""
Practica 2: Decorador
Ingenieria de Software
Emily Martinez Monroy
"""

"""
Funcion Decorador
"""
def my_decorador(f):
    def new_function(*args, **kwargs):
        print("Before Function")
        f(*args, **kwargs)
        print("After Function")
    return new_function

"""
Funcion para ejemplificar el decorador
"""
@my_decorador
def example_function(a,b,c):
    print(a)
    print(b)
    print(c)
