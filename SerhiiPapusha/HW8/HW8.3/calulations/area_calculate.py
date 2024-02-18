import math

def find_rectangele_area(width, length):
    area = width * length
    return f"Rectangele area is {area}"

def find_circle_area(radius):
    area = math.pi * pow(radius, 2)
    return f"Circle area is {area}"

def find_triangle_area(base, height):
    area = 0.5 * base * height
    return f"Triangle area is {area}"

__all__ = ['find_rectangele_area', 'find_circle_area', 'find_triangle_area']