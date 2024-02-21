
class Polygon:
    def __init__(self, sides):
        self.sides = sides


class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_area(self):
        return self.length * self.width


rectangle1 = Rectangle(5, 7)
print(f"Area of rectangle: {rectangle1.calc_area()}")
