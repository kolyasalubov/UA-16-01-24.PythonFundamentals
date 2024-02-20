class Polygon:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
 # rect area takes arguments fron Polygon and multiplicate it
class rect_area(Polygon):
    def multiplication(self):
        s = self.a * self.b
        return "The area of rectangle is: {}".format(s)

a = float(input("Enter the a: "))        
b = float(input("Enter the b: "))

p = rect_area(a,b)
print(p.multiplication())