####################################################################################################
#                                                                                                  #
#                  LICENCIA PÚBLICA PARA QUE HAGA LO QUE SEA QUE SE LE DÉ LA GANA                  #
#                                     Versión 1, enero de 2019                                     #
#                                                                                                  #
#    Derechos de autor (C) 2020 López Arias Víctor Ulises                                          #
#    Facultad de Ciencias, UNAM, CDMX, México                                                      #
#                                                                                                  #
#    Todos tienen permitido copiar y distribuir de forma literal o modificada copias de este       #
#    documento de licencia, y su modificación está permitida siempre que se le cambie el nombre.   #
#    Éste programa se entrega tal cual es y sin garantías de nada.                                 #
#                                                                                                  #
#                  LICENCIA PÚBLICA PARA QUE HAGA LO QUE SEA QUE SE LE DÉ LA GANA                  #
#                TÉRMINOS Y CONDICIONES PARA LA COPIA, DISTRIBUCIÓN Y/O MODIFICACIÓN               #
#                                                                                                  #
#    0. Tú solo HAZ LO QUE SEA, LO QUE TE DÉ LA GANA.                                              #
####################################################################################################
#                                                                                                  #
#                             Facultad de Ciencias, UNAM, CDMX, México                             #
#                                                                                                  #
#                                  Ingeniería de Software, 2020-2                                  #
#                                         Práctica 2                                               #
####################################################################################################


# Fuente: https://www.python-course.eu/python3_decorators.php
def my_decorator(funcion):
    """ Engloba la función para modificar su comportamiento.
    """
    def funcion_wrapper(x):
        """ Nos da calridad respecto a que sucedio primero.
        """
        print("Before function")
        res = funcion(x)
        print(res)
        print("After function")
    return funcion_wrapper

@my_decorator
def sucesor(n):
    """ El sucesor de un número.
    """
    return n + 1

sucesor(10)

#    López Arias Víctor Ulises      |       310173335       |       ulises.lopez@ciencias.unam.mx  #