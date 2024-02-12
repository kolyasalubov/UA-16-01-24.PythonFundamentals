# Writing a function that returns the largest number of two numbers

def return_largest_number(num1, num2):
    '''
       Takes 2 numbers and returns the largest one
       num1: int, float
       num2: int, float
    '''
    returning_string = "The largest number from entered ones is:"
    if num1 > num2:
        return (returning_string + f" {num1}")
    else:
        return (returning_string + f" {num2}")
    

print(return_largest_number(100, 3))
print(return_largest_number(59, 340))
print(return_largest_number(-100, 6))
print(return_largest_number(60.5, 60.4))
