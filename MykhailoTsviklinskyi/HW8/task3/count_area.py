__all__ = ["count_area_of_rectangle", "count_area_of_triangle", "count_area_of_circle"]

import math

def count_area_of_rectangle(width: float, length: float)->float:
    """This function counts area of rectangle with given width and length"""
    return width * length

def count_area_of_triangle(height: float, base: float)->float:
    """This function counts area of triangle with given height and base"""
    return 1/2 * height * base

def count_area_of_circle(radius: float)->float:
    """This function counts area of triangle with given radius"""
    return math.pi * math.pow(radius, 2)
