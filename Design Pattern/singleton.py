class Borg:
    """ Borg design pattern"""
    
    _shared_state = {}
    
    def __init__(self):
        self.__dict__ = self._shared_state

class Singleton(Borg):
    """ This class now shares all its attributes among its all variables by inheriting borg class"""
    
    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_state.update(kwargs)
    
    def __str__(self):
        return str(self._shared_state)



x = Singleton(HTTP = "hypertext transfer protocol")

print(x)

y = Singleton(SNMP = "Simple network management protocol")

print(y)