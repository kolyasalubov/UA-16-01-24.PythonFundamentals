# Creating a program which checks if user entered valid password

def is_password_valid(input_string): 
    '''Function checks if entered password is valid
       1. At least 1 letter between [a-z]
       2. At least 1 letter between [A-Z]
       3. At least 1 number between [0-9]
       4. At least 1 character from [$#@]
       5. Minimum length is 6 characters
       6. Maximum length is 16 characters
    
       type input_string: str
       
       returns True: if entered password is valid
       returns False: if entered password invalid
    '''

    