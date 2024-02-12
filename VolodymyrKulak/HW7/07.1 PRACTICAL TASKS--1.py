
def compare_nums(num1: int,
                 num2: int) -> str:
    """
    This func returns the largest number of two entered.
    :rtype: object
    :param num1: int
    :param num2: int
    :return: the argument that is bigger than other
    """
    if num1 > num2:
        return f"{num1} is bigger than {num2}"
    elif num1 < num2:
        return f"{num2} is bigger than {num1}"
    else:
        return "Entered numbers should not be equal"


print(compare_nums(55, 56))
