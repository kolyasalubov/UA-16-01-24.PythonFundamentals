temperature_in_celcius = float(input("Write the temperature in celcius: "))  # user's temperature in celsius 
temperature_in_Farenheit = (temperature_in_celcius* 9/5) + 32                # convert celsius into Farenheit
the_lowest = -273.15                                                         # the lowest temperature which is possible is -273.15 celsius


if temperature_in_celcius>the_lowest: 
    print(temperature_in_Farenheit)
else:
    print("Error: Temperature below absolute zero (-273.15°C)")
