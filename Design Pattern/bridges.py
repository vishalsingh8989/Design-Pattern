"""
parralle or diagnal abstraction
Implementation dependent circle abstraction

Implementation dependent circle abstraction
"""

class DrawingAPIOne(object):
    
    def draw_circle(self, x,y,radius):
        print("API 1 is drawing cicrle at  {} , {} , radius".format(x,y,radius))

class DrawingAPITwo(object):
    
    def draw_circle(self, x,y,radius):
        print("API 2 is drawing cicrle at  {} , {} , radius".format(x,y,radius))

class Circle(object):
    """ Implemenatation-independent
    """
    def __init__(self, x,y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api
    
    def draw(self):
        """ Implementation specific abstraction taken care of by another class DrawingApi
        """
        self._drawing_api.draw_circle(self._x, self._y, self._radius)
    
    def scale(self, percent):
        self._radius  *=  percent
        
        

circle1 = Circle(1,2,3, DrawingAPIOne())

circle1.draw()

circle2 = Circle(1,2,3, DrawingAPITwo())
circle2.draw()        
        
        