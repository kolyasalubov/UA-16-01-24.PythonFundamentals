def get_user_number():
    """This function gets user number from input"""
    user_number = int(input("Please enter your number: "))
    return user_number

def display_day_of_week(number: int):
    """
    This function displays the day of week according to
    the given number (1 is Monday, 2 is Tuesday, etc).
    If the given number is 8 or more than generate an exception
    """
    while True:
        if number in range(1, 8):
            if number == 1:
                print(f"Your number '{number}' is Monday")
                break
            elif number == 2:
                print(f"Your number '{number}' is Tuesday")
                break
            elif number == 3:
                print(f"Your number '{number}' is Wednesday")
                break
            elif number == 4:
                print(f"Your number '{number}' is Thursday")
                break
            elif number == 5:
                print(f"Your number '{number}' is Friday")
                break
            elif number == 6:
                print(f"Your number '{number}' is Saturday")
                break
            elif number == 7:
                print(f"Your number '{number}' is Sunday")
                break
        else:
            try:
                if number > 7:
                    raise ValueError(f"Your number '{number}' is greater than the number of days in the week. Try again")
            except ValueError as e:
                print(e)
                number = get_user_number()
            try:
                if number < 0:
                    raise ValueError(f"You entered negative value '{number}'. Try again")
            except ValueError as e:
                print(e)
                number = get_user_number()
            try:
                if number == 0:
                    raise ValueError(f"You entered zero value '{number}'. Try again")
            except ValueError as e:
                print(e)
                number = get_user_number()


while True:
    try:
        print("This program analyzes the entered number and, depending on the number, gives the day of the week that corresponds to this number (1 is Monday, 2 is Tuesday, etc.)")
        display_day_of_week(get_user_number())
        break
    except ValueError:
        print("You entered an incorrect value. Try again")
