digit = input("Enter 4-number digit:    ")
first_digit = int(digit[0])
second_digit = int(digit[1])
third_digit = int(digit[2])
fourth_digit = int(digit[3])
list_of_digits=[first_digit,
                second_digit,
                third_digit,
                fourth_digit
                ]
print(f'Production of the digits is {first_digit*second_digit*third_digit*fourth_digit}')
print(fourth_digit,third_digit,second_digit,first_digit,sep='')
list_of_digits.sort()
print(*list_of_digits,sep='')


