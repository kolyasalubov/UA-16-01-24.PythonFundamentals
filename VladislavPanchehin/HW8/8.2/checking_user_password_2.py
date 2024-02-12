#varaint 2

import re

# receive password from user
password = input('Enter your password: ')  

# check password length

def password_check(password):
    # regular expressions
    regular_expession = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,16}$"
    # regular expression pattern
    pattern = re.compile(regular_expession)
    # template matching check
    if re.search(pattern,password):
        return True
    else:
        return False
    
# checking and outputting the result
if password_check(password):
  print('Password is correct')
else:
  print('Password is not correct')  