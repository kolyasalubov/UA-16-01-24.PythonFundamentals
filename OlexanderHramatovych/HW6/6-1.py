list_of_even_numbers = [] #creating list for putting even numbers
list_of_odd_numbers = []  #creating list for putting odd numbers which are divisivle by 3
no_lists_numbers = []     #creating list for putting numbers which are divisivle  neither by 2  nor by 3

for number in range(1,10+1): # loop for the numbers
    if number % 2 == 0:
        list_of_even_numbers.append(number) # appending into the list even 
    elif number % 3 == 0:
        list_of_odd_numbers.append(number) # appending into the list odd 
    else:
        no_lists_numbers.append(number) # appending into the list other numbers

# outputting the resuly
print(f"Even numbers in range from 1 to 10 are: {list_of_even_numbers}")
print(f"Odd numbers which are divisible by 3 in range from 1 to 10 are: {list_of_odd_numbers}")
print(f"Numbers which are  divisible neither by 2 nor 3 in range from 1 to 10: {no_lists_numbers}")