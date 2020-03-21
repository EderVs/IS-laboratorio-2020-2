def hello_decorator(func):
	def inner1(*aguacate):
		print("╔════════════════════════════════════╗\n║ ♠ Este es el inicio de la función: ║\n╚════════════════════════════════════╝\n")

		func(*aguacate)

		mi = "\n╔════════════════════════════════════╗\n║ ♠ Este es el final de la función ♠ ║\n╚════════════════════════════════════╝\n"

		return str(func(*aguacate)) + "\n" + mi

	return inner1

@hello_decorator
def function_to_be_used(a, b):
	c = a + b
	#Si los marcos no se ven es culpa del Unicode >:v
	return c

print(function_to_be_used(2,2))