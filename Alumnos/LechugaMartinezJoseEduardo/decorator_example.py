from time import time


def eficiencia_decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes del decorador")
        t1 = time()
        resultado = func(*args, **kwargs)
        t2 = time()
        print(f"La funcion {func.__name__} tomo {t2 - t1}s en completarse")
        print("Despues del decorador")
        return resultado
    return wrapper


@eficiencia_decorador
def funcion_random():
    i = 1
    for i in range(0, 10000000):
        i*5
    return i


print(funcion_random())
