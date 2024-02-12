
import math

def rectangle_area(width: float, length: float) -> float:
    """
    This func calculates the area of the rectangle
    :param width: float
    :param length: float
    :return: the result of width * length
    """
    return width * length


def triangle_area(height: float, base: float) -> float:
    """
    This func calculates the area of the triangle
    :param height: float
    :param base: float
    :return: the result of the formula: (1/2 * height * base)
    """
    return 1/2 * height * base


def circle_area(radius: float) -> float:
    """
    This func calculates the area of the circle
    :param radius: float
    :return: the result of the formula: (PI * radius ** 2)
    """
    return math.pi * math.pow(radius,2)


__all__ = ['rectangle_area', 'triangle_area', 'circle_area']
