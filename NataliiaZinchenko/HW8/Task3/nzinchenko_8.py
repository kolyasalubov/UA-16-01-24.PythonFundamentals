from math import pow, pi


def rectangle_area_calculation(length, width):
    '''Function that calculates area of a rectangle by formula: 
       rectangle_area = length * width
       length: int / float
       width: int / float
    '''
    rectangle_area = length * width
    return rectangle_area


def triangle_area_calculation(base, height):
    '''Function that calculates area of a triangle by formula: 
       triangle_area = 0.5 * base * height
       length: int / float
       width: int / float
    '''
    triangle_area = 0.5 * base * height
    return triangle_area


def circle_area_calculation(radius):
    '''Function that calculates area of a circle by formula: 
       circle_area = PI * radius ** 2
       length: int / float
       width: int / float
    '''
    circle_area = pi * pow(radius, 2)
    return circle_area
