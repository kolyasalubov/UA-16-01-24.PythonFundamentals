
import re

loop_on = True
while loop_on:

    user_pass = input('Enter your password: ')

    pattern_1 = re.compile('[a-z]').findall(user_pass)
    pattern_2 = re.compile('[A-Z]').findall(user_pass)
    pattern_3 = re.compile('[\d]').findall(user_pass)
    pattern_4 = re.compile('[@#$]').findall(user_pass)
    pattern_5 = re.compile('[@#$]').findall(user_pass)

    if len(pattern_1) < 1:
        print('At least one letter between a-z')
    elif len(pattern_2) < 1:
        print('At least one letter between A-Z')
    elif len(pattern_3) < 1:
        print('At least one number between 0-9')
    elif len(pattern_4) < 1:
        print('At least one character from @ # $')
    elif len(user_pass) < 6:
        print('Minimum 6 characters')
    elif len(user_pass) > 16:
        print('Maximum length 16 characters')
    else:
        print('Your password is valid! You can proceed')
        loop_on = False
