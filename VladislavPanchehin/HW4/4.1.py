
temperature = int(input("Enter the temperature in Celsius:"))
converted_temperature = int((temperature * 9/5) + 32)
if temperature <= -273.15:
    print(f"Error: Temperature below absolute zero -273.15°C")
else:
    print(f"{temperature}°C is equivalent to {converted_temperature}F")


