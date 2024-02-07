# Writing 3 programs which calculate area of a rectangle, triangle and circle

def calculating_rectangle_area(length, width):
    '''Function that calculates rectangle area using length and width
       length: int OR float
       width: int OR float
    '''
    rectangle_area = length * width
    return rectangle_area


def calculating_triangle_area(base, height):
    '''Function that calculates triangle area using base and width
       base: int OR float
       width: int OR float
    '''
    triangle_area = (1/2) * base * height
    return triangle_area


def calculating_circle_area(radius):
    '''Function that calculates circle area using its radius
       radius: int OR float
    '''
    PI = 3.14159265
    circle_area = PI * radius ** 2
    return circle_area