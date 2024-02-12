number_pi = 3.14


def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return number_pi * radius ** 2


def area_calculation():
    print("1. Area of a rectangle")
    print("2. Area of a triangle")
    print("3. Area of a circle")
    user_choise = int(input("Enter your choise 1/2/3: "))

    if user_choise == 1:
        lenght = float(input("Enter the lengt of rectangle: "))
        weight = float(input("Enter the weight of rectangle: "))
        area = rectangle_area(lenght,weight)
        print("Area of a rectangle: ", area)

    elif user_choise == 2:
        base = float(input("Enter the base of triangle: ")) 
        height = float(input("Enter the height of a triangle: "))
        area = triangle_area(base,height)
        print("Area of a triangle ", area)

    elif user_choise == 3:
        radius = float(input("Enter the radius of circle: "))
        area = circle_area(radius) 
        print("Area of a cicrcle: ",area)   

    else:
        print("The choice is not correct!!!")

area_calculation()