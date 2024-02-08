user_input_degree = float(input("Enter the temperature in Celsius: "))
absolute_zero = -237.15
if user_input_degree < absolute_zero:
    print("Temperature below absolute zero (-237.15°C)")
else:
    converted_tempetarute = (user_input_degree * (9/5)) + 32
    print(f"{user_input_degree}°C is equivalent to {converted_tempetarute}°F")
    