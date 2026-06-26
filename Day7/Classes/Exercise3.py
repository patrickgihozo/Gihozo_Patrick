from abc import ABC, abstractmethod
class shapes(ABC):
    @abstractmethod
    def area(self):
        pass
class circle(shapes):
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        return 3.14* self.radius**2
        
class rectangle(shapes):
    def __init__(self,width,length):
        self.width = width
        self.length = length
    def area(self):
        return self.width *self.length
       
circle1 =circle(10)
rect1= rectangle(5,8)
print(circle1.area())
print(rect1.area())
