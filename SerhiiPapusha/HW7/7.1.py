def bigest_number(first_num, second_number):
    """This function will return largest number of two numbers entered 
    after it's sure that all numbers are integer""" 
    if isinstance(first_num, int) and isinstance(second_number, int):
        if first_num > second_number:
            return f"{first_num} is bigger then {second_number}"
        elif first_num < second_number:
            return f"{first_num} is less then {second_number}"
        else:
            return f"Numbers are equal"
    else:
        return "Make sure all the values are integers, script stopped"

print(bigest_number.__doc__)
print(bigest_number(9, 6))
print(bigest_number(8, "test"))