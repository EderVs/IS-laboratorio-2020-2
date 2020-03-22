import sys

def decorador(func):
	def dec(*args, **kwargs):
		print("Before function")
		func(*args, **kwargs)
		print("After function")
	return dec

@decorador
def noVocal(cadena):
	vocales = ("a", "e", "i", "o", "u")
	for x in cadena.lower():
		if x in vocales:
			cadena = cadena.replace(x, "")

	print(cadena)


noVocal(sys.argv[1])