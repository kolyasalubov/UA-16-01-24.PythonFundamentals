# Write a program that prompts the user to enter their age, and then displays a
# message stating whether the age is even or odd. The program must provide the ability
# to enter a negative number, and in this case generate an exception. The master code 
# should call a function that processes the information entered.

class CustomError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)

def is_age_even_or_odd(age):
        if age % 2 == 0:
            print(f"Entered age {age} is even")
        else:
            print(f"Entered age {age} is odd")

