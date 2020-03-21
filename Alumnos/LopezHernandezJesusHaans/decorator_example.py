'''
Author: Jesus Haans Lopez Hernandez

Practica 2 de Ingieneria de Software
'''
# Decorador que imprime before function antes de ejecutar cualquier funcion 
# y tambien imprime after function despues de ejecutar la funcion 

def decorator(f):
    def auxiliar_funtion(*args,**kwargs):
        print("*******************Before function*******************")
        f(*args,**kwargs)
        print("*******************After funtion*******************")
        return
    return auxiliar_funtion

# Un pequeño test para probar el decorador pero podemos usar 
# @decorator en cualquier funcion para darle el mismo formato

@decorator
def test(a,b,c):
    print(a)
    print(b)
    print(c)

#-----------Ejecucion de la prueba----------

test(1,2,300)
