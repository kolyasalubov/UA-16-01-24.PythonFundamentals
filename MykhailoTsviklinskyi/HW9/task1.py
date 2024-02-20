from random import randint

def generate_number_from_range_and_ask_to_guess(start_of_range = 1, end_of_range = 100, attempts = 10) -> int:
    """This function generate random number from given range and ask user to guess it using given attempts"""
    random_number = randint(start_of_range, end_of_range)
    attempt_counter = 1
    
    while attempts > 0:
        guess_number = int(input(f"Program generated random number from {start_of_range} to {end_of_range}. Try to guess it. {attempts} attempts left: "))
        if guess_number == random_number:
            print(f"Congratulation! The random number was {random_number}. You guessed it from {attempt_counter} attempt.")
            break
        elif guess_number > random_number:
            print(f"Your number '{guess_number}' is greated that the generated number.")
            attempts -= 1
            attempt_counter += 1
        elif guess_number < random_number:
            print(f"Your number '{guess_number}' is less that the generated number.")
            attempts -= 1
            attempt_counter += 1
    else:
        print(f"You used all {attempts} attempts but did not guess the number. The right number was {random_number}")

generate_number_from_range_and_ask_to_guess()
