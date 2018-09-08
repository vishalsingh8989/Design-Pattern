"""

processing request: decouple request and its processing
or not binding only one method for processing but deciding what to call based on processing request type.
"""

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


class ConcreteHandler1(Handler):
    
    def _handle(self, request):
        if 0 <=  request <  10:
            print("Request handled in handler 1".format(request))
            return True

class DefaultHandler(Handler):
    def _handle(self, request):
        print("End of chain, no handler for  {}".format(request))
    
class Client:
    
    def __init__(self):
        self.handler = ConcreteHandler1(DefaultHandler(None))
    
    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)
c = Client()

requests = [2,4,15]
c.delegate(requests)
            
        
        