from Formula import rectungle_area, triangle_area, circle_area

users_choise = input("Please choose a rectangle, triangle or circle to calculate an area? ").lower()

if users_choise == "rectangle":
    print(rectungle_area())

elif users_choise == "triangle":
    print(triangle_area())

elif users_choise == "circle":
    print(circle_area())
    
else:
    print("Wrong choise. Try again.")