
class Polygon:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rectangle(Polygon):
    
    def square (self):
        print(self.width * self.height) 
    
height = float(input('Enter height: '))
width = float(input('Enter width: '))

instance = Rectangle(width, height)

print(instance.square())