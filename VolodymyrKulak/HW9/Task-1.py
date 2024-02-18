
from random import randint

rand_num = randint(0, 100)
tries = 10

while tries > 0:

    user_num = int(input(f"You have {tries} tries to guess the random number, \n"
                         "Enter your number: "))
    tries -= 1

    if user_num < 0 or user_num > 100:
        print('Range for the random number is 0-100')
    elif user_num == rand_num:
        print(f'You guessed the random number!')
        break
    elif user_num > rand_num:
        print(f'Your number is higher than random number')
    elif user_num < rand_num:
        print(f'Your number is lower than random number')
else:
    print("Try again")
