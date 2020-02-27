def example(*args, **kwargs):
    print(args)
    print(kwargs["kwargs1"])

example("hola", 1, kwargs1="hola")