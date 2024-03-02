from math import pi, pow
def area_of_triangle(side :float,height:float) ->float:
    """
    Name: area_of_triangle
    input parameters: side, height
    type side: float
    type height: float
    function return float object
    """
    return pow(side*height,0.5)

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