input_value = int(input('Enter the temperature in Celsius: '))

if input_value > -273.15:
    print ((input_value * 9/5) +32)
else: print("error")