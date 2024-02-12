import math

def rectangle_area(side1, side2):
    area = side1*side2
    return area

def triangle_area(side, height):
    area = side*height/2
    return area

def circle_area(radius):
    area = math.pi * math.pow(radius, 2)
    return area