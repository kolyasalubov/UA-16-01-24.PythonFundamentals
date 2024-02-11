import nzinchenko_8 as areas


# Asking user which object area he wants to calculate
ask = input("Enter the object which area needs to be calculated (rectangle / triangle / circle): \n").lower()


if ask == "rectangle":
    ask_rectangle_length = areas.validation_and_conversion(input("Enter rectangle length: \n"))
    ask_rectangle_width = areas.validation_and_conversion(input("Enter rectangle width: \n"))
    result = areas.rectangle_area_calculation(ask_rectangle_length, ask_rectangle_width)
    print(f"Rectangle area: {areas.pretty_print(result)}\n")
elif ask == "triangle":
    ask_triange_base = areas.validation_and_conversion(input("Enter triangle base: \n"))
    ask_triangle_height = areas.validation_and_conversion(input("Enter triangle base: \n"))
    result = areas.triangle_area_calculation(ask_triange_base, ask_triangle_height)
    print(f"Triangle area: {areas.pretty_print(result)}\n")
elif ask == "circle":
    ask_circle_radius = areas.validation_and_conversion(input("Enter circle radius: \n"))
    result = areas.circle_area_calculation(ask_circle_radius)
    print(f"Circle area: {areas.pretty_print(result)}\n")
else:
    print("Unknown figure. Try again.\n")
