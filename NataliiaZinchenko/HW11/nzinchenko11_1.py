# Write a program that prompts the user to enter their age, and then displays a
# message stating whether the age is even or odd. The program must provide the ability
# to enter a negative number, and in this case generate an exception. The master code 
# should call a function that processes the information entered.

class CustomError(Exception):
    '''
    CustomError class to raise and catch custom exceptions
    '''
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


def is_age_even_or_odd(age):
    if age % 2 == 0:
        return f"Entered age {age} is even"
    else:
        return f"Entered age {age} is odd"


try:
    get_user_age = int(input("Enter your age to check if it's even or odd:\n"))
    if get_user_age < 0:
        raise CustomError(f"Entered age is {get_user_age}: can't be negative")
    elif get_user_age == 0:
        raise CustomError(f"Entered age is {get_user_age}: can't be 0")
    elif get_user_age > 105:
        raise CustomError(f"Entered age is {get_user_age}: can't be more than 105")
    print(is_age_even_or_odd(get_user_age))
except (ValueError, CustomError) as e:
    print(f"Exception: {e}")
    