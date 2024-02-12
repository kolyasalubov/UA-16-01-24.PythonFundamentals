
from HW8_TASK__3 import *

while True:
    user_figure = int(input("You are about to calculate the area of a geometric figure! \n"                      
                            "1 - is for Rectangle \n"
                            "2 - is for Triangle \n"
                            "3 - is for Circle \n"
                            "Please, select the figure by entering the number: \n"))

    if user_figure == 1:
        width = float(input("Enter rectangle's width: "))
        length = float(input("Enter rectangle's length: "))
        result_1 = rectangle_area(width, length)
        print(f"The area of the Rectangle is: {result_1}")
        break

    elif user_figure == 2:
        height = float(input("Enter triangle's height: "))
        base = float(input("Enter triangle's base: "))
        result_2 = triangle_area(height, base)
        print(f"The area of the Triangle is: {result_2}")
        break

    elif user_figure == 3:
        radius = float(input("Enter circle's radius: "))
        result_3 = circle_area(radius)
        print(f"The area of the Circle is: {result_3}")
        break

    else:
        print("Please, enter the number from 1-3")
        continue
