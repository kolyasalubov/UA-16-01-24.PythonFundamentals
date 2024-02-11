def largest(num1,num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Numbers are equals"

print(largest(100,1))