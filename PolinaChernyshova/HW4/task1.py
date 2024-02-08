Koliasa Liubov: good job
users_tempr = input('Please, enter the temperature in Celsius: ')

while not users_tempr.lstrip('-').replace('.','').isdigit() :
    users_tempr = input("Oh, we need a number. Try again: ")
users_tempr = float(users_tempr)

if users_tempr > -273.15:
    F = (users_tempr * 9/5) + 32
    print(f'{users_tempr}°C is equivalent to {round(F,2)}°F')
else:
    print(f'Error: Your temperature {users_tempr}°C below absolute zero (-273.15°C)')
