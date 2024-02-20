from random import randint


def guess_the_number(num):
    '''Function that generates random number and gives user 10 attempts to guess it.
       Function returns string with quantity attempts left or with congratulation message

       type num: str    
    '''
    num = int(num)
    random_number = randint(1,100)
    attempt = 1
    while attempt <= 10:
        if num == random_number:
            return f"You guessed random generated number {random_number}"


        elif num < random_number:
            print(f"This is your attempt {attempt} from 10")
            try_again = int(input("Your number is less than random generated one. Try again: \n"))
            num = try_again


        elif num > random_number:
            print(f"This is your attempt {attempt} from 10")
            try_again = int(input("Your number is bigger than random generated one. Try again: \n"))
            num = try_again

        attempt += 1
        print(f"Correct: {random_number}")
    return "Out of guesses"


user_guesses_number = input("Guess the random number from 1 to 100 and enter it here: \n")
print(guess_the_number(user_guesses_number))
