def solution(number):
    if number <= 0:
        return 0
    sum = 0
    for i in range(number):
        if i % 3 == 0 and i % 5 == 0:
            sum += i
        elif i % 3 == 0 or i % 5 == 0:
            sum += i
    
    return sum