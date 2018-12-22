class Korean:
    def __init__(self):
        self.name = "Korean"
    
    def speak_korean(self):
        return "An-yeong"

class British:
    def __init__(self):
        self.name = "British"
    
    def speak_british(self):
        return "Hello !!"



class Adapter:

    def __init__(self, object, **new_methods):
        self.__dict__.update(new_methods)
        self._object = object
#     def __init__(self, object, **adapted_method):
#         """
#         """
#         self._object = object
#         self.__dict__.update(adapted_method)
    
    def __getattr__(self, name):
        return getattr(self._object, name)


object = []
korean = Korean()
british = British()

object.append(Adapter(korean, speak=korean.speak_korean))
object.append(Adapter(british, speak=british.speak_british))

for obj in object:
    print("{} says.".format(obj.speak()))