# Write a program that analyzes the entered number and, depending on the number,
# gives the day of week that corresponds to this number (1 is Monday, 2 is Tuesday etc).
# Take into account cases of entering numbers from 8 and more, as well as cases of
# entering non-numerical data.

class CustomError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


def number_to_day(num):
    if num == 1:
        return "Monday"
    elif num == 2:
        return "Tuesday"
    elif num == 3:
        return "Wednesday"
    elif num == 4:
        return "Thursday"
    elif num == 5:
        return "Friday"
    elif num == 6:
        return "Saturday"
    elif num == 7:
        return "Sunday"
    
    
try:
    ask_number = int(input("Enter number from 1 to 7:\n"))
    if ask_number < 1:
        raise CustomError(f"You entered {ask_number}: Number can't be less than 1")
    elif ask_number > 7:
        raise CustomError(f"You entered {ask_number}: Number can't be more than 7")
    print(number_to_day(ask_number))
except (CustomError, ValueError) as e:
    print(f"Exception: {e}")
