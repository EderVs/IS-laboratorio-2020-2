def my_decorator(func):
	def aux(*args, **kwargs):
		print("Before function")
		func(*args, **kwargs)
		print("After function")
	return aux

@my_decorator
def example_function(a, b, c="c"):
	print(a)
	print(b)
	print(c)

example_function(1,2,c=3)