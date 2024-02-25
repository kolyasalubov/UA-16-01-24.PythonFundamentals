
def process_age(age):
    """This func processes the user's age and returns the value
    'even' or 'odd' correspondingly to the user's input or raises
    the ValueError if the input is negative"""

    if age < 0:
        raise ValueError("Age cannot be negative")

    if age % 2 == 0:
        return f"even"
    else:
        return "odd"


def main():
    try:
        age = int(input("Enter your age: "))
        result = process_age(age)
        print(f"Your age is {result}.")

    except ValueError as ve:
        print(f"Error: {ve}")


if __name__ == "__main__":
    main()
