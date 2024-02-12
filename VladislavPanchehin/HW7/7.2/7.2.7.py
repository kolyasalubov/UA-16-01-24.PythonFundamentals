def solution(number):
    #Initializing the total variable:
    total = 0
    #Loop to iterate through numbers from 1 to number-1:
    for item in range(1, number):
    #Checking the condition and accumulating the amount:    
        if item % 3 == 0 or item % 5 == 0:
            total += item
    return total


print(solution(10))