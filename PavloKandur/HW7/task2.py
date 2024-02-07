from math import pi
def area_of_triangle(side :float,height:float) ->float:
    """
    Name: area_of_triangle
    input parameters: side, height
    type side: float
    type height: float
    function return float object
    """
    return 0.5*side*height

def area_of_rectangle(side1:float,side2:float)->float:
    """
    Name: area_of_rectangle
    input parameters: side1, side2
    type side1: float
    type side2: float
    function return float object
    """
    return side1*side2

def area_of_circle(radius:float)->float:
    """
    Name: area_of_circle
    input parameters: radius
    type number1: float
    function return float object
    """
    return pi*radius*radius

user_choice = int(input("Select which area you want to calculate\n1.triangle\n2.rectangle\n3.circle\n"))
if user_choice == 1:
    data = input("Enter side and height: ").split()
    print(f"Area = {area_of_triangle(float(data[0]),float(data[1]))}")
elif user_choice == 2:
    data = input("Enter first and second sides: ").split()
    print(f"Area = {area_of_rectangle(float(data[0]),float(data[1]))}")
elif user_choice == 3:
    data = float(input("Enter radius: "))
    print(f"Area = {area_of_circle(data)}")
else:
    print("Wrong input")