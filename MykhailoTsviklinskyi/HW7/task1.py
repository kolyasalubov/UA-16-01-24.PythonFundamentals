def get_largest_number(number_1: int, number_2: int)->int:
    """This function returns the largest number of two numbers"""
    return max(number_1, number_2)

number_1 = int(input("Please enter first natural number: "))
number_2 = int(input("Please enter second natural number: "))
    
print(f"The largest number of {number_1} and {number_2} is:", get_largest_number(number_1, number_2))
