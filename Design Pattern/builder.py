class Director:
    """Director """
    
    def __init__(self, builder):
        self._builder = builder
    
    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()
    
    def get_car(self):
        return self._builder.car

class Builder():
    """Abstract class """
    
    def __init__(self):
        self.car = None
    
    def create_new_car(self):
        self.car = Car()

class SkyLarkBuilder(Builder):
    """ concrete builder - > provides tools and parts to work  on the parts"""
    
    def add_model(self):
        self.car.model = "SkyLark"
    
    def add_tires(self):
        self.car.tires = "Regular tires"
        
    def add_engine(self):
        self.car.engine  = "turbo"
        
class FordBuilder(Builder):
    """ concrete builder - > provides tools and parts to work  on the parts"""
    
    def add_model(self):
        self.car.model = "FORD"
    
    def add_tires(self):
        self.car.tires = "Fancy tires"
        
    def add_engine(self):
        self.car.engine  = "V8 Engine"

class Car:
    """"""
    
    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None
    def __str__(self):
        return "{} {} {}".format(self.model, self.tires, self.engine)

builder = SkyLarkBuilder()
fordbuilder = FordBuilder()
director = Director(builder)
director.construct_car()
print(director.get_car())
director = Director(fordbuilder)
director.construct_car()
print(director.get_car())


    
    
        
        