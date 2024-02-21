class Polygon():
    def __init__(self, num_of_sides):
        self.n = num_of_sides
        self.sides = [0 for i in range(self.n)]
    
    def input_sides(self):
        self.sides = [float(input(f"Side {i+1}:")) for i in range(self.n)]

class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)
    
    def find_area(self):
        a, b = self.sides
        area = a * b
        print(f"Area: {area}")

rectangle = Rectangle()
rectangle.input_sides()
rectangle.find_area()