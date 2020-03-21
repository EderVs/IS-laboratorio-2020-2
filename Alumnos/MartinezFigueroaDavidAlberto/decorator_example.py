#Decorador Ejemplo
def funcion_decorador(funcion_p):

    def funcion_interna(*args, **kwargs):
        print("Before Function")
	
        funcion_p(*args, **kwargs)
    		
        print("After Function")
	

    return funcion_interna


#Prueba

@funcion_decorador
def resta(num1,num2):
    print(num1-num2)


resta(num2=30,num1=3)

resta(30,3)


