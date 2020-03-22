#Autor: Oscar Fernando Millan Pimentel

#Decorador
def msgDecorator(f):
    def fun(*args, **kwargs):
        print("Before Function")
        f(*args, **kwargs)
        print("After Function\n")
    return fun

#funcion suma con decorador
@msgDecorator
def suma(a,b):
    return a+b

#funcion multiplicacion con decorador
@msgDecorator
def multi3 (a,b,c):
    return a*b*c

#funcion example_function con decorador
@msgDecorator
def example_function(a,b,c="c"):
    print(a)
    print(b)
    print(c)

#Ejecuciones
print(suma(4,5))
multi3(2,3,4)
example_function(1,2,3)