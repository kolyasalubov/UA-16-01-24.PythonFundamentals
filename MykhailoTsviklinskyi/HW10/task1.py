class Polygon:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Rectangle(Polygon):
    def calculate_square_of_rectangle(self):
        """
        This function calculates square of rectangle using length and width
        variables given in inherited class Polygon
        """
        square_of_rectangle = self.length * self.width
        return f"Square of rectangle with length {self.length} and width {self.width} is: {square_of_rectangle}"

length = float(input("Please enter length of rectangle: "))
width = float(input("Please enter width of rectangle: "))

instance1 = Rectangle(length, width)

print(instance1.calculate_square_of_rectangle())
