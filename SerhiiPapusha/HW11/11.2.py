# first variant
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
days_of_week_dict = {}

for index, day in enumerate(days_of_week):
    key = index + 1
    value = day
    days_of_week_dict[key] = value

print(days_of_week_dict)

try:    
    day_number = input("enter number from 1 to 7 that corresponds to proper day of week\n")
    if not day_number.isdigit():
        raise ValueError("Input must be a number!")
    day_number = int(day_number)
    if int(day_number) > 7 or int(day_number) < 1:
        raise ValueError("Number cannor be less then 1 or bigger then 7")
    else:
        print(days_of_week_dict[int(day_number)])
except ValueError as e:
    print(e)

# second variant
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
days_of_week_dict = {index + 1: day for index, day in enumerate(days_of_week)}
print(days_of_week_dict)

try:    
    day_number = input("enter number from 1 to 7 that corresponds to proper day of week\n")
    if not day_number.isdigit():
        raise ValueError("Input must be a number!")
    day_number = int(day_number)
    if 1 <= day_number <= 7:
        print(days_of_week_dict[day_number])
    else:
        raise ValueError("Should be a number from 1 to 7!")
except ValueError as e:
    print("Error:", e)
