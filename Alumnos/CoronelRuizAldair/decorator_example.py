#-------------------------------------------------
# Ingeniera de Software
# Profesor: Hanna Jadwiga Oktaba
# Ayudante de lab: Eder Vázquez Salcedo
#
# Aldair Coronel Ruiz | Práctica 2
# - Decoradores -
# Usando el mismo decorador para cualquier función
#-------------------------------------------------


def my_decorator(function_to_decorate):
    """
     *args and **kwargs are used to accept an
     arbitrary number of positional and keyword
     arguments
    """
    def wrapper(*args, **kwargs):
        print("Before function")
        function_to_decorate(*args, **kwargs)
        print("After function")
    return wrapper

@my_decorator # Syntactic sugar
def multiples_of_n_in_range_i_j(i, j, n=3):
    # My example function
    for x in range(i, j + 1): # Inclusive range end
        if x % n == 0:
            print(x," is multiple of ",n)

@my_decorator # Syntactic sugar
def example_funtion(a, b, c="c"):
    # Example function given in the practice specification
    print(a)
    print(b)
    print(c)


# Executions
print("My example function")
multiples_of_n_in_range_i_j(0, 30, n=5)
print("")
print("Example function given in the practice specification")
example_funtion(1, 2, c=3)
