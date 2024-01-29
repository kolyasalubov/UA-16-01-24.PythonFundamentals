celsius = input("Enter the temperature in Celsius: ")

if float(celsius) <= -273.15:
    print("Error: Temperature below absolute zero (-273.15°C)")
    exit()

fahrenheit_formula = (int(celsius) * (9/5) + 32)
print(f"{celsius}°C is equivalent to {fahrenheit_formula}°F")
