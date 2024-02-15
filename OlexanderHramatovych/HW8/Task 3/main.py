from geometric_calculator import rectangle_area
from geometric_calculator import triangle_area
from geometric_calculator import circle_area


while True:
    ask = input("Hello, what area do you want to calcualte or? \nTriangle,Rectangle or Circle \n Or do you want to exit: ")
    if ask == ("Rectangle"):
        rec_side1 = float(input("Enter the first side of rectangle: "))
        rec_side2 = float(input("Enter the second side of rectangle: "))
        print(rectangle_area(rec_side1,rec_side2))
    elif ask == ("Triangle"):
        tr_hight = float(input("Enter the height of triangle: "))
        tr_side = float(input("Enter the cathetus of triangle: "))
        print(triangle_area(tr_hight,tr_side))
    elif ask == ("Circle"):
        radius = float(input("Enter the radius of circle: "))
        print(circle_area(radius))
    elif ask == ("exit"):
        print("See you soon :)")
        break
    else:
        print("There is not {} areas".format(ask))