from abc import ABC, abstractmethod

# TODO: multipe inheritance and abstract base classes (interface)

from abc import ABC, abstractmethod

class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass

class GraphicsShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass

class Circle(GraphicsShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14*(self.radius**2)

    def toJSON(self):
        return f"{{\" Circle \" : {str(self.calcArea())}  }}"

class Square(GraphicsShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side*self.side


# g = GraphicsShape()
c = Circle(10)
print(c.calcArea())
print(c.toJSON())