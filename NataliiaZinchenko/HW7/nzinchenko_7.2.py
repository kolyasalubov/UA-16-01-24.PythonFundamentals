# Writing program which calculate area of a rectangle, triangle or circle


def calculate_rectangle_area(length, width):
    '''Function that calculates rectangle area using length and width
       length: int OR float
       width: int OR float
    '''
    rectangle_area = length * width
    return rectangle_area


def calculate_rectangle_area_console():
    '''Function that printing out the result of rectangle area calculation,
       depending on the data type of rectangle's length & width (int / float)
    '''
    print("Ok! Let's calculate rectangle area!\n")
    custom_rectangle_length = float(input("Enter rectangle length: \n"))
    custom_rectangle_width = float(input("Enter rectangle width: \n"))


    output_rectangle_area = calculate_rectangle_area(custom_rectangle_length, custom_rectangle_width)
    

    if output_rectangle_area - int(output_rectangle_area) > 0:
        print(f"Rectangle area is: {output_rectangle_area:.2f}")
    else:
        output_rectangle_area = int(output_rectangle_area)
        print(f"Rectangle area is: {output_rectangle_area}")


def calculate_triangle_area(base, height):
    '''Function that calculates triangle area using base and width
       base: int OR float
       width: int OR float
    '''
    triangle_area = (1/2) * base * height
    return triangle_area


def calculate_triangle_area_console():
    '''Function that printing out the result of triangle area calculation,
       depending on the data type of rectangle's base & height (int / float)
    '''
    print("Ok! Let's calculate triangle area!\n")
    custom_triangle_base = float(input("Enter triangle base: \n"))
    custom_triangle_height = float(input("Enter triangle height: \n"))

    
    output_triangle_area = calculate_triangle_area(custom_triangle_base, custom_triangle_height)

    
    if output_triangle_area - int(output_triangle_area) > 0:
        print(f"Triangle area is: {output_triangle_area:.2f}")
    else:
        output_triangle_area = int(output_triangle_area)
        print(f"Triangle area is: {output_triangle_area}")


def calculate_circle_area(radius):
    '''Function that calculates circle area using its radius
       radius: int OR float
    '''
    PI = 3.14159265
    circle_area = PI * radius ** 2
    return circle_area


def calculate_circle_area_console():
    '''Function that printing out the result of circle area calculation
    '''
    print("Ok! Let's calculate circle area!\n")
    custom_triangle_radius = float(input("Enter radius of the circle: \n"))


    output_circle_area = calculate_circle_area(custom_triangle_radius)
    print(f"Circle area is: {output_circle_area:.2f}\n")


choosing_object = input("Which object's area you want to calculate (Rectangle, triangle or circle): \n").lower()
if choosing_object == "rectangle":
    calculate_rectangle_area_console()
elif choosing_object == "triangle":
    calculate_triangle_area_console()
elif choosing_object == "circle":
    calculate_circle_area_console()
else:
    print("Entered data is incorrect. Try again.")
