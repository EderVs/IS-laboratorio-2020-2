# López Soto Ramses Antonio 31531997-4
## Ejemplo de un decorador simple


def decorator(func):
    def function(*args):
        print("Before function")
        func(*args)       
        return repr(func(*args)) + "\nAfter funtion"
    return function

## Ejemplo 1
@decorator
def suma(a, b):
    return a + b

print(suma(4, 6))

print("------------------")

## Ejemplo 2
@decorator
def mayor3(a, b, c):
    if (a > b) and (a > c):
        return a
    if (b > a) and (b > c):
        return b
    else: 
        return c

print(mayor3(2, 15, 7))

print("------------------")

@decorator
def imprimeHola():
    return "Wola!"

print(imprimeHola())
