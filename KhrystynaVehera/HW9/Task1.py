import random 

def guess_number():
    rand_number = random.randint(1, 100)
    tries = 0   
    user_number = int(input("We generate randomly a number. Please guess this number in 10 tries: "))
    while tries <= 10:
        if rand_number > user_number:
            tries+=1
            print(f"Your number {user_number} is less than generate number. You have {10-tries} tries more." )
            
        elif rand_number < user_number:
            tries+=1
            print(f"Your number {user_number} is greater than generate number. You have {10-tries} tries more." )
            
        elif rand_number == user_number:
            tries+=1
            print(f"Congratulate, you win. Generated number is {rand_number}." )
            break
        
        user_number1 = int(input("Try again: "))
        user_number = user_number1

    else:
        print("Game over. You already used 10 tries.")


guess_number()
