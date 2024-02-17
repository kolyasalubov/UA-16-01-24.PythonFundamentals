import random

random_number = random.randint(1, 100)
start_point = 0
NUMBERS_OF_ATTEMPS = 10

user_name = input("Enter your name: ")
print(f"Hello,", user_name, '\n' "Guess the number! You have 10 attempts")


while start_point < NUMBERS_OF_ATTEMPS:
    user_number = int(input("Enter your number:  \n"))
    start_point += 1

    if user_number == random_number:
        print("Congratulation", user_name, "YOU WIN!!! \n")
        break

    elif user_number < random_number:
        print("Try entering a number less \n")
        print(
            f"Attempts used {start_point}\nAttempts left  {NUMBERS_OF_ATTEMPS - start_point} \n")

    elif user_number > random_number:
        print("Try entering a higher number \n")
        print(
            f"Attempts used {start_point}\nAttempts left {NUMBERS_OF_ATTEMPS - start_point} \n")
    else:
        print("The number is not guessed")

print(
    f"Attempts used: {start_point}\nAttempts left: {NUMBERS_OF_ATTEMPS - start_point}")

if start_point == NUMBERS_OF_ATTEMPS:
    print("Sorry, you have used all attempts. The number was:", random_number, '\n')
