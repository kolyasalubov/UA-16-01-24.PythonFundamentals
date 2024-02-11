# varian 1


# receive password from user
password = input('Enter your password: ')  

# check password length

def password_check(password):
   if len(password) < 6 or  len(password) > 16:
      return False
   
# check for lowercase letters  
    
   if not any (word.islower() for word in password):
    return False
# check for capital letters
   if not any (word.isupper() for word in password):
     return False
# checking for numbers 
   if not any (word.isdigit() for word in password):
     return False
# checking for characters [$#@]   
   if not any (word in ['$','#','@'] for word in password):
     return False
# if all checks pass, password correct
   return True
# checking and outputting the result
if password_check(password):
  print('Password is correct')
else:
  print('Password is not correct')  

  
   
     


