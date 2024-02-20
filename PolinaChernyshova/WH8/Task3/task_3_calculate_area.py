import math

def calculate_area_rectangle(side_a: float, side_b: float )->float:
    '''
    The function takes to float type arguments: side_a, side_a
    Return the area of a rectangle in float type 
    '''
    return side_a * side_b

def calculate_area_triangle(side_a: float, height: float )->float:
    '''
    The function takes to float type arguments: side_a, height
    Return the area of a triangle in float type 
    '''
    return 0.5 * side_a * height

def calculate_area_circle(radius: float)->float:
    
    '''
    The function takes to float type argument: radius
    Return the area of a circle in float type 
    '''
    return math.pi * math.pow(radius,2)
