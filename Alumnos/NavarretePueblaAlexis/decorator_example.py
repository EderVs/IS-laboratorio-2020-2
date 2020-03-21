#Navarrete Puebla Alexis
#
def my_decorator(func):
    def wrapper(*args, **kargs):
        print("--------------------Before function--------------------")
        try:
        	func(*args, **kargs) #Se manda a llamar la función del parámetro, por ende imprime la suma de los tres parámetros
        except Exception as e:
        	
        	print("Parámetros no numéricos, abortando")
        	return
        print("--------------------After function--------------------")
    return wrapper

@my_decorator
def suma(a , b, c="c", **kargs):
	res = int(a)+int(b)+int(c)
	print("El resultado de la suma es: " + str(res))	

suma(1,2, c=3, d = "1")
