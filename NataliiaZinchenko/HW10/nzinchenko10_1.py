# Creating a polygon class and a rectangle class and finding square of rectangle

class Polygon:
    '''
    Class Polygon with base and height properties and area() method
    '''
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height
    
class Rectangle(Polygon):
    '''
    Class Rectangle which inherits properties from Polygon class
    '''
    def __init__(self, base, height):
        super().__init__(base, height)
