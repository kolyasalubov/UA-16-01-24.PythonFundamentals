temperature_celsius = float(input("Enter a temperature in Celsius: "))

ABSOLUTE_ZERO = -273.15

temperature_fahrenheit = (temperature_celsius * 9/5) + 32

print(f"Entered the temperature in Celsius: {temperature_celsius}")

if temperature_celsius >= ABSOLUTE_ZERO:
    print(f"{temperature_celsius}°C is equivalent to {temperature_fahrenheit:.2f}°F")
else:
    print(f"Error: Temperature below absolute zero ({ABSOLUTE_ZERO})")

# I decided to make float() instead of int() and add limit ':.2f' because it's too long value after comma when the temperature_celsius is for example -273.15 or 36.6
