# Práctica 2 de Ingeniería de Software
# Gutiérrez Velázquez Héctor Ernesto

import functools

# Definimos el decorador.
def my_decorator(func):
    @functools.wraps(func)
    def envoltura(*args, **kwargs):
        print("Before function")
        resultado = func(*args, **kwargs)
        print("After function")
        return resultado
    return envoltura

# Un ejemplo del uso del iterador
@my_decorator   
def test1(a, b, c=0):
    print("Recibí: {}, {}, {}".format(a, b, c))
    print("El resultado es {}".format(a+b-c))
    return a + b - c

test1(22, 9, 6)
