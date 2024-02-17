import random

NUMBERS_OF_ATTEMPTS = 10


def launch_guessing_game():
    """
    Username request and random number generation

    """
    user_name = input("Enter your name: ")
    print(f"Hello,{user_name}!\nGuess the number! You have 10 attempts")
    return random.randint(1, 100)


def get_user_guess():
    """
    Receiving a number from the user

    """
    try:
        user_number = int(input("Enter your number: "))
        return user_number

    except ValueError:
        print("Enter a valid number")
        return None


def check_guess(random_number, user_number, attempt_count):
    """
    Checking for guessing the number and displaying information in the remaining attempts.

    """
    if user_number == random_number:
        print("Congratulation! YOU WIN\n")
        return True
    elif user_number < random_number:
        print("Try entering a higher number.\n")
    else:
        print("Try entering a lower number.\n")

    print(
        f"Attempts used: {attempt_count}\nAttempts left: {NUMBERS_OF_ATTEMPTS - attempt_count}\n")
    return False


def run_game():

    random_number = launch_guessing_game()
    start_point = 0

    while start_point < NUMBERS_OF_ATTEMPTS:
        user_number = get_user_guess()
        if user_number is None:
            continue

        start_point += 1
        if check_guess(random_number, user_number, start_point):
            break

    if start_point == NUMBERS_OF_ATTEMPTS:
        print("Sorry, you have used all itempts. The number was:", random_number)


# run
run_game()
