def the_lagest(*arc):
    """
    Function for funding the lagest number between two numbers.
    
    Parameters:
    *arc: necesarry amount of input numbers, current - two numbers
    
     Returns:
    number: Return the lagest number in the string result + "is largest number".
    
    """
    number = 0

    for i in arc:
        while i > number:
            number = 0
            number = i
        else: 
            continue

    return f"{number} is the lagest number."

print(the_lagest(5, 32))