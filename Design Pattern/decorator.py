from functools import wraps


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
def hello_word():
    """original function"""
    return "hello world"


print(hello_word())
print(hello_word.__name__)
print(hello_word.__doc__)
