
user_num = int(input("Enter the number to make factorial of: "))

factorial = 1

if user_num < 0:
   print("Sorry, factorial can not be from negative numbers")
elif user_num == 0:
   print("The factorial of 0 is 1")
else:
   for item in range(1, user_num + 1):
       factorial = factorial*item
print(f'{user_num}! = {factorial}')
