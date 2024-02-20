import re

user_name = input("Please enter your password: ")


def validator(user_name):
    big_letter = re.findall("[A-Z]", user_name)
    little_letter = re.findall("[a-z]", user_name)
    number_in = re.findall(r"\d", user_name)
    symbol_in = re.findall("[$#@]", user_name)

    if len(big_letter) >= 1 and len(little_letter) >= 1 and len(number_in) >= 1 and len(symbol_in) >= 1 and 16>len(user_name)>6:
        return "Congratulation, format of your password is correct."
    else:
        return ("In your password should be SMALL letter, BIG letter, at least one NUMBER and one of this SYMBOLS $#@." +
        "\nDont forget!!! Your paasword should be LONGER than 6 items but SHOTTER than 16!!!")
    

validator(user_name)
print(validator(user_name))
