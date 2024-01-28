Celcius =float( input("Enter temperature in celcius: "))
if Celcius >= -273.15:
    print(Celcius,"°С is equivalent to ", (Celcius * 9/5)+32, "°F")
else:
     print ("Error: Temperature below absolute zero (-273.15°C)")