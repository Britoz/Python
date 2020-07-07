'''
Abstract file
Author: The Vinh Ly

Descript: using abstract
using ABC library
'''

# TODO: using abstract in python

from abc import ABC, abstractmethod

class GraphicsShape(ABC):
    def __init__(self):
        super().__init__()

    '''
    super() used to call the 
    '''

    @abstractmethod
    def calcArea(self):
        pass

# TODO:
#
class Circle(GraphicsShape):
    def __init__(self, radius):
        self.radius = radius

    """
    radius: input parameter for class
    """

    def calcArea(self):
        return 3.14*(self.radius**2)
    '''
    3.14 is PI value
    Area of Circle is PI*radius^2
    '''

class Square(GraphicsShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side*self.side

    '''
    
    '''


# g = GraphicsShape()
c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())