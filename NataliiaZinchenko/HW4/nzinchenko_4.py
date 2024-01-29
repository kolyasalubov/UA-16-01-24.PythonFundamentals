first_number = input("Enter the 1st number: ")
second_number = input("Enter the 2nd number: ")


if not (first_number.replace("-","").isnumeric() and second_number.replace("-","").isnumeric()):
    print("Entered values should be numeric")
    exit()


first_number = int(first_number)
second_number = int(second_number)


if first_number > second_number:
    print(f"{first_number} is more than {second_number}")
elif first_number < second_number:
    print(f"{second_number} is more than {first_number}")
elif first_number == second_number:
    print(f"Entered numbers are equal")