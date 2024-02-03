list_of_even_numbers = []
list_of_odd_numbers = []
no_lists_numbers = []

for number in range(1,10+1):
    if number % 2 == 0:
        list_of_even_numbers.append(number)
    elif number % 3 == 0:
        list_of_odd_numbers.append(number)
    else:
        no_lists_numbers.append(number)
print(f"Even numbers in range from 1 to 10 are: {list_of_even_numbers}")
print(f"Odd numbers which are divisible by 3 in range from 1 to 10 are: {list_of_odd_numbers}")
print(f"Numbers which are  divisible neither by 2 nor 3 in range from 1 to 10: {no_lists_numbers}")