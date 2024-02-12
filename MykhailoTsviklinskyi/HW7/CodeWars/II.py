# Find The Distance Between Two Points
# https://www.codewars.com/kata/simple-find-the-distance-between-two-points

def distance(x1, y1, x2, y2):
    result = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return round(result, 2)
    