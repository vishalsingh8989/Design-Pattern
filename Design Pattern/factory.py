class Dog:
    """ A simple dog class"""

    def __init__(self, name= "Hope"):
        self._name = name
    
    def __str__(self):
        return "Dog"
    def speak(self):
        return "Woof!"


class DogFactory:
    """ Concrete factory"""
    def get_pet(self):
        """ """
        return Dog()
    
    def get_food(self):
        return "Dog food!"
    

class PetStore:
    """ """
    
    def __init__(self, pet_factory = None):
        """ pet factory"""
        self._pet_factory = pet_factory
    
    def show_pet(self):
        """ """
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()
        print("Our pet is '{}'!".format(pet))
        print("Our pet always say hello by  '{}'".format(pet.speak()))
        print("Its food is '{}'".format(pet_food))
        
class Cat:
    """ A simple cat class"""

    def __init__(self, name):
        self._name = name
    
    def speak(self):
        return "Meow!"

def get_pet(pet = "dog"):
    
    """The factory method"""
    
    pets = dict(dog = Dog("Hope"), cat = Cat("Peace"))
    
    return pets[pet]



factory  = DogFactory()
shop = PetStore(factory)


shop.show_pet()
# dogobj = get_pet("dog")
# print(dogobj.speak())   
# catobj = get_pet("cat")
# print(catobj.speak())  



