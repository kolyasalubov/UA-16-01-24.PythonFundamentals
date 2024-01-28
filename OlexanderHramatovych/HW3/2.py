# Task №1
number = input("Type four-digital number: ")                              # user's number
first_task = int(number[0])*int(number[1])*int(number[2])*int(number[3])  # converting number to integer
print(first_task)                                                         # printing out the answer



# Task №2
reversed_numbers = number[::-1]
print(reversed_numbers)

# Task №3
sorted_numbers = sorted(number)
print(sorted_numbers)