class Polygon:
    def __init__(self, num_of_sides):
        self.num_of_sides = num_of_sides
        self.sides = [0 for i in range(num_of_sides)]

    def inputSides(self):
        self.sides = [float(input(f"Input side {str(i+1)}:")) for i in range(self.num_of_sides)]

    def showSides(self):
        for i in range(self.num_of_sides):
            print(f"Side #{i+1} is {self.sides[i]}")

class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)
    
    def calculateRectArea(self):
        a, b = self.sides
        area = a * b
        return f"Your rectangle area is {area}"

obj1 = Polygon(4)
# obj1.inputSides()
# obj1.showSides()

obj2 = Rectangle()
obj2.inputSides()
print(obj2.calculateRectArea())