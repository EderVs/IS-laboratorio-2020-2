def decorator(decorada):
	def interna(*args):
		print ("before function")

		decorada(*args)

		print ("after function")

	return interna

@decorator
def example(a,b):
	print(a)
	print(b)

example(1,2)
