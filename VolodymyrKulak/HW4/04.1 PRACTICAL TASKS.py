
user_temp_Cels = float(input("Enter your temperature in Celsius "))
temp_in_Fahr = 0

if user_temp_Cels < -273.25:
    print("Temperature below absolute zero (-273.15)")
else:
    temp_in_Fahr = (user_temp_Cels * 9/5) + 32
    print(user_temp_Cels, 'is equivalent to ', temp_in_Fahr, 'F')
