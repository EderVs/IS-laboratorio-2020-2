def decorator_holatarolas(func):
  def wrapper(*args, **kargs):
    print("Holas vienen")
    func(*args,**kargs)
    print("Holas van")
    
  return wrapper

@decorator_holatarolas
def fun():
  print("¡Hola!")
  
@decorator_holatarolas
def funargs(arg1,arg2, arg3 = "soy_3"):
  print(arg1, arg2, arg3)
  return arg1
  
fun()
funargs("chido", "neta", "ya wey")
 
 
#Protocolo de tranferencia de hipertexto
	## request methods to indicate someone we want to use its resources
	## códigos que indican el estado de la respuesta (llegó ono, ther wasa problem, etc)
	## servidor webb
	## django framework para web app en python
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
