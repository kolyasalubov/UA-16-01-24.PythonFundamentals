temperature_in_celsius = float(input('Enter the temperature in Celsius: '))
temperature_in_fahrenheit = (temperature_in_celsius * 9/5) + 32
ABSOLUTE_ZERO = -273.15

if temperature_in_celsius >= ABSOLUTE_ZERO:
    print(f"Temperature in Celsius {temperature_in_celsius} C is equivalent to {temperature_in_fahrenheit} F")
else:
    print(f"Temperature is below absolute zero {ABSOLUTE_ZERO}")