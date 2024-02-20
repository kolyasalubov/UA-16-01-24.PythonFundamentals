import random


RANDON_NUMBER = random.randint(1,100)

ATTEMPTS = 10

def guess_number():
    '''
    Function name -> guess_number()
    Arguments -> None
    Return type -> None, Void
    About: User can input number and guess the number, what chous randomly. 
    User has 10 attempts
    '''
    global ATTEMPTS
    tmp = 1
    user_number = 0
    while ATTEMPTS != 0:
        user_number = int(input('Hello, input your number, which you think is the same with us. \nDisclaimer: You have only 10 attempts'
                            + f'\nYour {tmp} attempt' + '\nThe number must be between 1 to 100: '))
        if user_number == RANDON_NUMBER:
            print('You wiiiiiin))))')
            break
        if ATTEMPTS == 1 and user_number !=RANDON_NUMBER:
            print(f'You lose, our number is {RANDON_NUMBER}')
            break
        elif user_number < RANDON_NUMBER:
            print('You don\'t guess, try again. Your number was less than our one')
        else:
            print('You don\'t guess, try again. Your number was greater than our one')
        print('')
        tmp+=1
        ATTEMPTS -= 1


if __name__ == "__main__":
    guess_number()