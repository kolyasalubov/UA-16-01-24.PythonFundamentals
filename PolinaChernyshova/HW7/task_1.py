
def returned_largest_number(num1: float, num2: float)-> float:
    '''
    The function takes to float type arguments: num1, num2
    Return the largest float type number between to arguments
    '''
    return max(num1, num2)




user_num1 = float(input("Enter a first number for compare: "))
user_num2 = float(input("Enter a second number for compare: "))

largest_num = returned_largest_number(user_num1, user_num2)

print(f'The largest number between {user_num1} and {user_num2} is {largest_num}')
