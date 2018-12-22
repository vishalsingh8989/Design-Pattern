"""
need for dynamically changing an behaivuor of class
"""

import types # support dynamic creation of types

class Strategy:
    
    def __init__(self, function = None):
        self.name = "Default"
        if function:
            self.execute = types.MethodType(function, self)
        
    
    def execute(self):
        print("{} is used".format(self.name))
    
# replacement method 1
def strategy_one(self):
    print("{} is used to execute method 1".format(self.name))

def strategy_two(self):
    print("{} is used to excecute method 2".format(self.name))


s0 = Strategy()
s0.execute()

s1 = Strategy(strategy_one)
s1.execute()

s2 = Strategy(strategy_two)
s2.execute()


