users_choise = input("Please choose a rectangle, triangle or circle to calculate an area? ").lower()


def rectungle_area():
    a = int(input("Please enter width: "))
    b = int(input("Please enter length: "))
    area = a * b
    return (f"The area of your rectangle is {area}")


def triangle_area():
    a = int(input("Please enter side: "))
    h = int(input("Please enter height: "))
    area = 0.5*a*h
    return (f"The area of your circle is {area}")


def circle_area():
    r = int(input("Please enter radius: "))
    area = (r**2) * 3.14
    return (f"The area of your circle is {area}")


if users_choise == "rectangle":
    print(rectungle_area())
elif users_choise == "triangle":
    print(triangle_area())
elif users_choise == "circle":
    print(circle_area())
else:
    print("Wrong choise. Try again.")