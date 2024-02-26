class Polygon:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def triangleArea(self):
        return self.a * self.b


class Triangle(Polygon):
    def __init__(self, a, b):
        super().__init__(a, b)
    

    

a=Triangle(3, 4)
print(a.triangleArea())