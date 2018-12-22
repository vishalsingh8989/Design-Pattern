"""

processing request: decouple request and its processing
or not binding only one method for processing but deciding what to call based on processing request type.
"""



from abc import abstractmethod, ABCMeta

class Chain:
    __metaclass__ = ABCMeta
    @abstractmethod
    def handle(self):
        print("Default handler")

class NegativeNumber(Chain):
    
    
    def __init__(self, handle = None):
        self._handle = handle
    
    def handle(self, req):
        if req < 0:
            print("Number is negative")
        else:
            self._handle.handle(req)
            
class ZeroNumber(Chain):
    def __init__(self, handle = None):
        self._handle = handle
    
    def handle(self, req):
        if req == 0:
            print("Number is Zero")
        else:
            self._handle.handle(req)

class PositiveNumber(Chain):
    def __init__(self, handle = None):
        self._handle = handle
    
    def handle(self, req):
        if req > 0:
            print("Number is Positive")
        else:
            self._handle.handle(req)


c = PositiveNumber(ZeroNumber(NegativeNumber()))

    
c.handle(10)
c.handle(0)
c.handle(-10)

class Handler:
    
    def __init__(self, succesor):
        self._succesor = succesor
    
    def handle(self, request):
        """
        """
        
        handled = self._handle(request)
        if not handled:
            self._succesor._handle(request)
    
    def _handle(self, request):
        raise NotImplementedError("must provide implementation")


class BasicHandler(Handler):
    
    def _handle(self, request):
        if request ==  4:
            print("Request handled in handler BasicHandler :{}".format(request))
            return True
        self._succesor._handle(request)
        return False
    
class ConcreteHandler(Handler):
    
    def _handle(self, request):
        if  request ==  2:
            print("Request handled in handler ConcreteHandler : {}".format(request))
            return True
        return False

class DefaultHandler(Handler):
    
    def _handle(self, request):
        print("End of chain, no handler for  {}".format(request))
    
class Client:
    
    def __init__(self):
        self.default = DefaultHandler(None)
        self.basic = BasicHandler(self.default)
        self.handler = ConcreteHandler(self.basic)
    
    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)

# c = Client()
# 
# requests = [2,4,5,15, 20]
# c.delegate(requests)
            
        
        