celsius_temp = float(input("Enter the temperature in Celsius: "))


if celsius_temp > -273.15:
    fahrenheit = round((celsius_temp * 9/5) + 32, 2)
    print(f"{celsius_temp}°C is equivalent to {fahrenheit}°F")
else:
    print(f"Sorry, your temperature is unavailable for converting. Please try again.")
    