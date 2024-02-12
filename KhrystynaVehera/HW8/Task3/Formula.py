from math import pi, pow

def rectungle_area():
    a = int(input("Please enter width: "))
    b = int(input("Please enter length: "))
    area = a * b

    return (f"The area of your rectangle is {area}")


def triangle_area():
    a = int(input("Please enter side: "))
    h = int(input("Please enter height: "))
    area = pow(a*h,2)

    return (f"The area of your circle is {area}")


def circle_area():
    r = int(input("Please enter radius: "))
    area = (r**2) * pi

    return (f"The area of your circle is {area}")