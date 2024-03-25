def distance(x1, y1, x2, y2):
    x = x2-x1
    y = y2-y1
    d = ((x ** 2)+(y ** 2))**0.5
    return round(d,2)
print(distance(1,1,0,0))