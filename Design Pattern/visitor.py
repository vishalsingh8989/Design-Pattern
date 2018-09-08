"""

Adding new feature to existing class hiarchrchy without changing.
"""


class House(object):
    def __init__ (self, houseno = ""):
        self._houseno = houseno
        
    def accept(self, visitor):
        """ Interface to acceot a visitor """
        visitor.visit(self)
    
    
    def work_on_hvac(self, hvac_specialist):
        print(self, "worked on by", hvac_specialist)
    
    def work_on_electricity(self, electrician):
        print(self, "worked on by", electrician)
    
    def __repr__(self):
        return self._houseno
    
    def __str__(self):
        return self._houseno


class Visitor(object):
    """Abstract visitor
    """
    
    def __repr__(self):
        return self._name
    
    def __str__(self):
        return self._name
    
class HvacSpecialist(Visitor):
    
    def __init__(self, name):
        self._name = name
        
    def visit(self, house):
        house.work_on_hvac(self)
        
class Electrician(Visitor):
    
    def __init__(self, name):
        self._name = name
    
    def visit(self, house):
        house.work_on_electricity(self)



hv = HvacSpecialist("Davis")

elec = Electrician("Megan")

house = House("House 1206")

house.accept(hv)

house.accept(elec)
