class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides

    # def print_info(self):
        # print(f"Sides of a polygon {self.num_sides}")

# class and heritage

class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(4)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# test creating object (rectangle)
size_of_rectangle = Rectangle(10, 20)
# inherited class Polygon
# print("Sides", size_of_rectangle.num_sides)
# print(type(size_of_rectangle))
# Calculated
print("Area of Rectangle:", size_of_rectangle.area())
