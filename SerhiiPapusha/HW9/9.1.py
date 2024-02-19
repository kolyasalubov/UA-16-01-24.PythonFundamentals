import random

def guess_number():
    num_to_guess = random.randint(1, 100)
    counter = 0
    print(num_to_guess)
    while counter < 10:
        print(f'Attempt # {counter + 1}')
        user_guess = int(input('Gues the number from 0 to 100:\n'))
        if user_guess != num_to_guess:
            print(f'Failed, you have {10 - (counter + 1)} more attempts')
            counter += 1
            continue
        else:
            print('You have guessed the number, congrats!')
            return True
    print(f'Sorry you have ran out of attempts')
    return False

guess_number()