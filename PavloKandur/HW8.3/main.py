from AreasFormula import area_of_circle, area_of_rectangle, area_of_triangle

user_choice = int(input("Select which area you want to calculate\n1.triangle\n2.rectangle\n3.circle\n"))
if user_choice == 1:
    data = input("Enter side and height: ").split()
    print(f"Area = {area_of_triangle(float(data[0]),float(data[1]))}")
elif user_choice == 2:
    data = input("Enter first and second sides: ").split()
    print(f"Area = {area_of_rectangle(float(data[0]),float(data[1]))}")
elif user_choice == 3:
    data = float(input("Enter radius: "))
    print(f"Area = {area_of_circle(data)}")
else:
    print("Wrong input")
