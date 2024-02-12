def rectangle_area(side1, side2):
    area = side1*side2
    return area

def triangle_area(side, height):
    area = side*height/2
    return area

def circle_area(radius):
    area = 3.14 * radius**2
    return area

choice = int(input("Choose the figure (1 - rectagle, 2 - triangle, 3 - circle): "))

if choice == 1:
    side1 = int(input("Side1: "))
    side2 = int(input("Side2: "))
    print("Area:", rectangle_area(side1, side2))
if choice == 2:
    side = int(input("Side: "))
    height = int(input("Height: "))
    print("Area:", triangle_area(side, height))
if choice == 3:
    radius = int(input("Radius: "))
    print("Area:", circle_area(radius))