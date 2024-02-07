# Writing 3 programs which calculate area of a rectangle, triangle and circle


def calculating_rectangle_area(length, width):
    '''Function that calculates rectangle area using length and width
       length: int OR float
       width: int OR float
    '''
    rectangle_area = length * width
    return rectangle_area


def calculating_triangle_area(base, height):
    '''Function that calculates triangle area using base and width
       base: int OR float
       width: int OR float
    '''
    triangle_area = (1/2) * base * height
    return triangle_area


def calculating_circle_area(radius):
    '''Function that calculates circle area using its radius
       radius: int OR float
    '''
    PI = 3.14159265
    circle_area = PI * radius ** 2
    return circle_area


choosing_object = input("Which object's area you want to calculate (Rectangle, triangle or circle): \n").lower()
if choosing_object == "rectangle":
    print("Ok! Let's calculate rectangle area!\n")
    custom_rectangle_length = input("Enter rectangle length: \n")
    custom_rectangle_width = input("Enter rectangle width: \n")


    if "." in custom_rectangle_width and custom_rectangle_length:
        custom_rectangle_length = float(custom_rectangle_length)
        custom_rectangle_width = float(custom_rectangle_width)
    else:
        custom_rectangle_length = int(custom_rectangle_length)
        custom_rectangle_width = int(custom_rectangle_width)

    output_rectangle_area = calculating_rectangle_area(custom_rectangle_length, custom_rectangle_width)
    
    if type(custom_rectangle_length) and type(custom_rectangle_width) == float:
        print(f"Rectangle area is: {output_rectangle_area:.2f}")
    else:
        print(f"Rectangle area is: {output_rectangle_area}")


#elif choosing_object == "triangle":
#    print("Ok! Let's calculate triangle area!\n")
#    custom
