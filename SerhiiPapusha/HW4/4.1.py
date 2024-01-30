# Temparature converter

celsius_temp = input('Enter temperature in Celsius: ')
# print(type(celsius_temp))

if celsius_temp.replace("-", "").isdigit():
    celsius_temp = int(celsius_temp)
    absolute_zero = -273.15

    if celsius_temp > absolute_zero:
        fahreheit_temp = (celsius_temp *9/5) + 32
        print(f'{celsius_temp} C is equivalent to {fahreheit_temp} F')
    elif int(celsius_temp) < absolute_zero:
        print(f'Error: Temperature below absolute zero')
else:
    print(f'Error: Must enter a valid number')