
#1---------------------------------------------------------------
#PRODUCT OF THE 4-DIGITAL NUMBER

digit = input("Enter four-digit number: ")

digit1 = int(digit[0])
digit2 = int(digit[1])
digit3 = int(digit[2])
digit4 = int(digit[3])

digit_list=[digit1, digit2, digit3, digit4]
result = digit1 * digit2 * digit3 * digit4
print("Result of product of the 4-digit number is", result)

#2---------------------------------------------------------------
#REVERSE ORDER OF THE 4-DIGITAL NUMBER

reversed_digit = digit[::-1]
print("Reversed 4-digit number is", reversed_digit)


#2---------------------------------------------------------------
#REVERSE ORDER OF THE 4-DIGITAL NUMBER

sorted_digit = sorted(digit)
print("Sorted  4-digit number is", sorted_digit)
