from math import pow, pi

def validation_and_conversion(num):
    '''Function that validates if entered value is:
       1. Is not negative
       2. Is numeric
       3. Is not 0
       4. Either float or int
    '''
    if "-" in num:
        raise Exception("Entered value can't be less than 0")
    
    if not num.replace(".", "").isdigit():
        raise Exception("Entered value is not numeric")

    if "." in num:
       num = float(num)
    else:
       num =  int(num)

    if num <= 0:
        raise Exception("Entered value can't be 0")
    
    return num


def pretty_print(num):
    '''Returns either float rounded up to 2 decimals digits
       or returns int without decimals digits
    '''
    if float(num) - int(num) > 0:
        return f"{num:.2f}"
    
    return int(num)

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
    