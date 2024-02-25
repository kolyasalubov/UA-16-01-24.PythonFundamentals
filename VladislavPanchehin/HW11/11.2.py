# Main function
def age_even_or_odd(user_age, user_name):
    if user_age < 0:
        raise ValueError("ERROR! - The entered number is negative!")

    if user_age % 2 == 0:
        return (f"'{user_name}' your Age: '{user_age}' is even")
    else:
        return (f" User:'{user_name}' your Age: '{user_age}' is odd")

# Global logic programm. Input age and name
def main():
    try:
        user_name = (input("User enter your name: "))
        user_age = int(input("Enter your age: "))
        result = age_even_or_odd(user_age, user_name)
        print(result)
    except ValueError as e:
        print(e)

# Run programm
run = main()
