def decorador(func):
    def nuevafuncion(*args,**kargs):
        print ("La funcion se esta ejecutando")
        func(*args,**kargs)
        print("La funcion acaba de terminar")
    return nuevafuncion

@decorador
def funcionImprime(a,b):
    print("EL primer parametro es " + str(a) )
    print("EL segundo parametro es " + str(b) )
    return "adios"


x=[1,2,3,4,5]
y=[6,7,8,9,0]
funcionImprime(x,y)
