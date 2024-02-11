import nzinchenko_8 as areas


# Asking user which object area he wants to calculate
ask = input("Enter the object which area needs to be calculated (rectangle / triangle / circle): \n").lower()


if ask == "rectangle":
    ask_rectangle_length = int(input("Enter rectangle length: \n"))
    ask_rectangle_width = int(input("Enter rectangle width: \n"))
    result = areas.rectangle_area_calculation(ask_rectangle_length, ask_rectangle_width)
    print(f"Rectangle area: {result}\n")
elif ask == "triangle":
    ask_triange_base = int(input("Enter triangle base: \n"))
    ask_triangle_height = int(input("Enter triangle base: \n"))
    result = areas.triangle_area_calculation(ask_triange_base, ask_triangle_height)
    print(f"Triangle area: {result}\n")
elif ask == "circle":
    ask_circle_radius = int(input("Enter circle radius: \n"))
    result = areas.circle_area_calculation(ask_circle_radius)
    print(f"Circle area: {result}\n")
else:
    print("Something went wrong. Try again.")
