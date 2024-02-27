days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Satuday','Sunday']
try:
    user_input = int(input("Enter number of the day to display: "))
    print(days[user_input-1])
except IndexError:
    print("Number too big")
except ValueError:
    print("Wrong input, must be digit")