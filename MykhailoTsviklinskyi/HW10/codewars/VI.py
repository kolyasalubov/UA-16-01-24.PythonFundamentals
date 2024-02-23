# Dynamic Classes
# https://www.codewars.com/kata/55ddb0ea5a133623b6000043

import string

def class_name_changer(cls, new_name):

    if new_name[0] not in string.ascii_uppercase:
        raise Exception("Name has to start with uppercase letter")

    for item in new_name:
        if item not in string.ascii_letters and item not in string.digits:
            raise Exception("Allow only names with alphanumeric chars")

    cls.__name__ = new_name
