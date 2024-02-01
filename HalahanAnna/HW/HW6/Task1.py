numb_two = [num for num in range(1, 11) if num % 2 == 0]

numb_three = [num for num in range(1, 11) if num % 2 == 1 and num % 3 == 0]

other_numb = [num for num in range(1, 11) if num % 2 != 0 and num % 3 != 0]

print("even numbers divisible by 2:", numb_two)
print("odd numbers divisible by 3:", numb_three)
print("numbers not divisible by 2 and 3:", other_numb)

