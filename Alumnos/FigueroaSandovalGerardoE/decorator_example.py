def decorator(func):
  def interna(*args,**kwargs):
    print("Haremos una ejecucion")

    valor = func(*args,**kwargs)

    print("La ejecucion a terminado")

    return valor
  return interna

@decorator
def suma(a, b):
  print("La ejecucion ahora es una Suma")
  return a + b

@decorator
def multi(a,b):
    print("La ejecucion ahora es una Multiplicacion")
    return a * b


print(suma(1,2))
print(multi(5,2))
