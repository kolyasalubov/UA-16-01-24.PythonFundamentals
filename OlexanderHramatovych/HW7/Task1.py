#creating the function which definds which number is largest
def largest(num1,num2):
    if num1 > num2: # creating the conditions
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Numbers are equals"

print(largest(100,1))