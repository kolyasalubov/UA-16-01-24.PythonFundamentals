import re


bool_tmp = True
while bool_tmp:
    user_login = input(
        "\nEnter your login \nDisclaimer: Your login can has \nAt least 1 letter between [a-z] "
        + "and 1 letter between [A-Z]"
        + "\nAt least 1 number between [0-9]."
        + "\nAt least 1 character from [$#@]."
        + "\nMinimum length 6 characters."
        + "\nMaximum length 16 characters"
        + "\nSo, your login: "
    )

    login_length = len(user_login) >= 6 and len(user_login) <= 16
    upper_letter = len(re.findall("[A-Z]", user_login)) >= 1
    lower_letter = len(re.findall("[a-z]", user_login)) >= 1
    number_in_loggin = len(re.findall("\d", user_login)) >= 1
    specific_character = len(re.findall(r"[@#$]", user_login)) >= 1

    if (
        login_length
        and upper_letter
        and lower_letter
        and number_in_loggin
        and specific_character
    ):
        print("You create correct login\n")
        bool_tmp = False
    else:
        print("Something goes wrong, you miss some rules\n")
