
even_numbers = []
odd_numbers = []
other_numbers = []

for num in range(1, 11):
    if num % 2 == 0:
        even_numbers.append(num)
    elif num % 3 == 0:
        odd_numbers.append(num)
    else:
        other_numbers.append(num)

print(f'Even numbers divisible by 2 are: {even_numbers}', '\n',
      f'Odd numbers divisible by 3 are: {odd_numbers}', '\n',
      f'Numbers that are not divisible by 2 and 3 are: {other_numbers}')
