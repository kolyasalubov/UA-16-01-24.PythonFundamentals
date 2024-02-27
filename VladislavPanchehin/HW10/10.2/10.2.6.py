# variant 1

import re


def class_name_changer(cls, new_name):
    cls.__name__ = new_name


class My_Class():
    print('This is My_Class')


# variant 2


def class_name_changer(cls, new_name):
    pattern = re.compile(r'^[A-Z][a-zA-Z0-9_]*$')
    if pattern.match(new_name):
        cls.__name__ = new_name
    else:
        raise ValueError(
            "Invalid class name: Only uppercase letters, digits, and underscores are allowed, and the name must start with an uppercase letter")


class My_Class:
    print('This is My_Class')


# Test case
try:
    class_name_changer(My_Class, "Invalid_Class$")
    print("No error occurred")
except ValueError as e:
    print(e)
