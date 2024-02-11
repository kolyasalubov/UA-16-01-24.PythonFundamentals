from area_calculator import rectangle_area, triangle_area, circle_area


def main():

    print("1. Area of a rectangle")
    print("2. Area of a triangle")
    print("3. Area of a circle")


# while True:
    user_choise = int(input("Enter your choise 1/2/3: "))

    if user_choise == 1:
        lenght = float(input("Enter the lengt of rectangle: "))
        weight = float(input("Enter the weight of rectangle: "))
        area = rectangle_area(lenght, weight)
        print("Area of a rectangle: ", area)
        # break
    elif user_choise == 2:
        base = float(input("Enter the base of triangle: "))
        height = float(input("Enter the height of a triangle: "))
        area = triangle_area(base, height)
        print("Area of a triangle ", area)
        # break
    elif user_choise == 3:
        radius = float(input("Enter the radius of circle: "))
        area = circle_area(radius)
        print("Area of a cicrcle: ", round(area))
        # break
    else:
        print("The choice is not correct!!!")


main()
