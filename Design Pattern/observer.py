"""

when a subject to be monitored by multiple observers

one to many relationship

Subject: abstract class
  Attach observer
  Detach observer
  Notify observer
"""

class Subject(object):
    #represent
    
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        """
        Attach an observer
        """
        if observer not in self._observers:
            self._observers.append(observer)
    
    def dettach(self, observer):
        try:
            self._observer.remove(observer)
        except ValueError:
            pass
    
    def notify(self, modifier = None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


class Core(Subject):
    
    def __init__(self, name = ""):
        Subject.__init__(self)
        self._name = name
        self._temp = 0
        
    @property
    def temp(self):
        return self._temp
    
    @temp.setter
    def temp(self, temp):
        self.notify()
        self._temp = temp


class TeamViewer:
    
    """ """
    def __init__(self, name=""):
        self._name = name
        
    def update(self, subject):
        """ invoked when notify is called
        """
        print("Temperature viewer in {} notified : {} has temperature {}".format(self._name, subject._name, subject._temp))



core = Core("ShriHariKota")

obs1 = TeamViewer("Delhi")
obs2 = TeamViewer("Mumbai")
obs3 = TeamViewer("Chennai")

core.attach(obs1)
core.attach(obs2)
core.attach(obs3)


core.temp = 90 # this will automatically trigger all the observer notify methods

core.temp = 80 # this will automatically trigger all the observer notify methods



        
        
        
        
