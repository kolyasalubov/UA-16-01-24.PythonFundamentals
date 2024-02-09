# Multiples of 3 or 5
# https://www.codewars.com/kata/multiples-of-3-or-5

def solution(number):
    list = ()

    for item in range(1, number):
        if item % 3 == 0 or item % 5 == 0:
            list += (item,)

    return sum(list)
