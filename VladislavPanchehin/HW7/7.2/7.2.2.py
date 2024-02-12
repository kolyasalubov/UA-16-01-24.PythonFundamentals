import math

def distance(x1, y1, x2, y2):

    distance_squared_pow = pow((x2 - x1), 2) + pow((y2 - y1), 2)
    distance_squared_pow_sqrt = math.sqrt(distance_squared_pow)

    return round(distance_squared_pow_sqrt,2)


print(distance(1, 1, 0, 0))

