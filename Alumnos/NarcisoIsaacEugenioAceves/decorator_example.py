def my_decorator(this_is_a_name): 
    #Decorator that prints stuff
    
    def inner1(*args, **kwargs):
        #Function to recover arguments passed to decorated function
        print("Before function")
        try:
            eduardo_eder = this_is_a_name(*args, **kwargs)
        except Exception as e:
            print("  function did not work correctly, Python says that: \n    "+ str(e))
        finally:
            print("After function")
        return eduardo_eder 
        
    return inner1


@my_decorator
def cute_print(a, b, c=3):
    #Simple function to print stuff
    print(str(a) + " " + str(b) + " " + str(c)) 
    return 0
  
#Function call to showcase decorator
cute_print("Hola","EduardoEder.vs")
