import random

riddled_number = random.randint(0,100)
counter_of_tries = 0

while counter_of_tries < 10:
    user_input = int(input("Enter the number: "))
    counter_of_tries += 1
    if user_input == riddled_number:
        print(f"Congratulation, you have won")
    elif user_input > riddled_number:
        print(f"Riddled number are lower, you have {10-counter_of_tries} tries left")
    elif user_input < riddled_number:
        print(f"Riddled number are higher, you have {10-counter_of_tries} tries left")
else:
    print("You didn't guess")
