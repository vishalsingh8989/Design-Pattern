class Borg:
    """ Borg design pattern. only attributes are shared. two objects are created in different memory"""
    
    _shared_state = {}
    
    def __init__(self):
        self.__dict__ = self._shared_state

class SingletonByBorg(Borg):
    """ This class now shares all its attributes among its all variables by inheriting borg class"""
    
    def __init__(self, **kwargs):

        Borg.__init__(self)
        self._shared_state.update(kwargs)
    
    def __str__(self):
        return str(self._shared_state)


class Singleton(object):
    
    __instance = None
 
    def __new__(cls, *args, **kwargs):
        
        if Singleton.__instance is None:
            Singleton.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
            
        return Singleton.__instance
        
    def __init__(self):
        """ Virtually private constructor. """
        
  
         
s = Singleton()
print s

s = Singleton()
print s

s = Singleton()
print s

s = Singleton()
print s


x = SingletonByBorg(HTTP = "hypertext transfer protocol")

print(x)

y = SingletonByBorg(SNMP = "Simple network management protocol")
print(y)


#print(hash(x), hash(y))