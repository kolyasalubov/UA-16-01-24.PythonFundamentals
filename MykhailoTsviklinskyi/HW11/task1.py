def get_user_age():
    """This function gets user age from input"""
    user_age = int(input("Please enter your age: "))
    return user_age

def display_even_or_odd(age: int):
    """
    This function displays if the given age is even or odd.
    If the given age is a negative number than generate an exception
    """
    while True:
       if age > 0:
            if age % 2 == 0:
               print(f"Your age number '{age}' is even")
               break
            elif age % 2 == 1:
               print(f"Your age number '{age}' is odd")
               break
       else:
            try:
                if age < 0:
                    raise ValueError(f"You entered negative value '{age}'. Try again")
            except ValueError as e:
                print(e)
                age = get_user_age()
            try:
                if age == 0:
                    raise ValueError(f"You entered zero value '{age}'. Try again")
            except ValueError as e:
                print(e)
                age = get_user_age()

while True:
    try:
        display_even_or_odd(get_user_age())
        break
    except ValueError:
        print("You entered an incorrect value. Try again")
