class Polygon():
    pass

class Rectangle(Polygon):
    def __init__(self,side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def rectangle_square(self):
        return self.side_a * self.side_b
    
my_rec = Rectangle(2,4)
print(my_rec.rectangle_square())