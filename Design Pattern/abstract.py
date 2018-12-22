
from abc import ABCMeta, abstractmethod


class AbstractExpression:
    
    __metaclass__ = ABCMeta
    
    
    @abstractmethod
    def intrepret(self):
        pass


class Hello(AbstractExpression):
    def execute(self):
        print("Execute in hello")
    
    def intrepret(self):
        print("intrepret in hello")
    

h = Hello()
h.execute()
print(vars(h))