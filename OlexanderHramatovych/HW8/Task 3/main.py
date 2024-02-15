from geometric_calculator import rectangle_area
from geometric_calculator import triangle_area
from geometric_calculator import circle_area
# import functions from the calcualator

# creating the loop
while True:
    ask = input("Hello, what area do you want to calcualte or? \nTriangle,Rectangle or Circle \n Or do you want to exit: ") # asking the user about which area to calculate and does he want to exit
    if ask == ("Rectangle"):
        rec_side1 = float(input("Enter the first side of rectangle: "))  # user enters the numbers
        rec_side2 = float(input("Enter the second side of rectangle: "))
        print(rectangle_area(rec_side1,rec_side2)) # outputting the result
    elif ask == ("Triangle"):
        tr_hight = float(input("Enter the height of triangle: ")) # user enters the numbers
        tr_side = float(input("Enter the cathetus of triangle: "))
        print(triangle_area(tr_hight,tr_side))                  # outputting the result
    elif ask == ("Circle"):
        radius = float(input("Enter the radius of circle: ")) # user enters the numbers
        print(circle_area(radius))  # outputting the result
    elif ask == ("exit"): # if user wants to exit
        print("See you soon :)")
        break   # break the loop
    else:
        print("There is not {} areas".format(ask))  # if user's shape is not in program