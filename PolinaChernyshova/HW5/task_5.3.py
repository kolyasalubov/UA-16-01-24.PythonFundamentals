# Write a script that will calculate the factorial 
# of the entered number without using pecursion

user_num = int(input('User, please, input number for calculate the factorial: '))
while user_num < 0:
    user_num = int(input("Sorry, but the factorial can only be calculated for a positive number. Try again: "))

help_num = factorial_num = 1

while help_num <= user_num:
    if user_num == 0:
        break
    else:
        factorial_num *= help_num
        help_num += 1
        
print(f'Factorial of your number {user_num} equal to {factorial_num}')
