import math
from math import pow
from math import pi 

def rectangle_area(first_side_of_rectangle:float,second_side_of_rectangle:float)->float:
    return first_side_of_rectangle * second_side_of_rectangle
def triangle_area(hight_of_triangle:float,cathetus:float)->float:
    return 0.5 * hight_of_triangle * cathetus
def circle_area(radius):
    return(radius ** 2) * pi

