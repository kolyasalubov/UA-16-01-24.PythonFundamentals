# 5.3 Calculating the factorial of entered number

entered_number = int(input("Enter a number to create factorial: "))

n = 1
k = ""
if entered_number < 2:
    print(f"{entered_number}! = {entered_number}")
else:
    for x in range (1, entered_number+1):
        n = n * x
        k += (f"{str(x)}")
        if x < entered_number:
            k += " * "

    print(f"{entered_number}! = {k} = {n}")
