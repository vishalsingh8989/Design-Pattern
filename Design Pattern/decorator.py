from functools import wraps
import time



def exe_time(function):
    
    
    def wrapper():
        start = time.time()
        ret  = function()
        print("Time taken : {0}".format(time.time() - start))
        return ret

def make_blink(function):
    
    #this makes decorator transparent in terms of its name and docstring
    # otherwise docstring of the decorator will be added to docstring of the original fucntion on fxn.__name__ call
    @wraps(function)
    
    def decorator():
        """ decorator docstring"""
        ret  = function()
        return  "<blink>" + ret + "</blink>" 
    return decorator
   
@make_blink    
@exe_time
def hello_word():
    """original function"""
    return "hello world"


print(hello_word())

