import math

def rectangle_area():
    length = float(input('Enter length: '))
    width = float(input('Enter width: '))
    return length * width

def triangle_area():
    base = float(input('Enter base: '))
    height = float(input('Enter height: '))
    return (base * height)/2

def circle_area():
    radius = float(input('Enter radius: '))
    return math.pi * math.pow(radius, 2)



