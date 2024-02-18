from calulations import *


def calculate_figures_area():
    while True:
        figure = input(f"""Enter which figure you would like to count area for - 1 for rectangele, 
                             2 for circle, 
                             3 for triangle\n""")
        match figure:
            case "1":
                width = int(input(f"Please enter rectangele width and length to calculate, width?: \n"))
                length = int(input(f"length?: \n"))
                print(find_rectangele_area(width, length))
            case "2":
                radius = int(input(f"Please enter circle radius to calculate: \n"))
                print(find_circle_area(radius))
            case "3":
                base = int(input(f"Please enter triangle base and height to calculate, base?: \n"))
                height = int(input(f"height?: \n"))
                print(find_triangle_area(base, height))
        check_if_proceed = input("""Would you like to proceed or finish the script?\n
                                press 'y' for yes and 'n' for now\n""")
        if check_if_proceed != "y":
            break

calculate_figures_area()
