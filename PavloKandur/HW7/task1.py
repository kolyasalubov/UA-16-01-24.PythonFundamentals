def largest_number(number1 :int, number2 :int) ->int:
    """
    Name: largest_number
    input parameters: number1, number2
    type number1: int
    type number2: int
    function return int object
    """
    if number1 > number2:
        return number1
    elif number2 > number1:
        return number2
    else:
        return f"Numbers are equal"
    
print(largest_number(5,5))
print(largest_number.__doc__)