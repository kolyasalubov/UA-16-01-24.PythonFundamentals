def largest_number(num, num1):
    """
    Finds the largest number among two given numbers.

    Parameters:
    num (int): first number.
    num1 (int): second number.

    Returns:
    tuple: A tuple containing the string "The largest number" and 
    the result largest number.

    """
    max_largest_number = max(num, num1)
    return "The largest number", max_largest_number

#Example
print(largest_number(5, 15))

# variant 2


def largest_number(num1, num2):
    """
    Finds the largest number among two given numbers.

    Parameters:
    num1 (int): The first number.
    num2 (int): The second number.

    Returns:
    int: The largest number among the two input numbers.
    """
    return max(num1, num2)


# Example
print(largest_number(5, 10))
