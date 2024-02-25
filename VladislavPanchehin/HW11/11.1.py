# Create function and dict days of week

def day_of_week(num):
    days_of_week = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sanday'
    }

    try:

        num = int(num)
        if num < 0:
            return "Enter a number greater than 0."

        elif num <= 7:
            return days_of_week[num]

        else:
            return "There are 7 days in a week"

    except:
        ValueError
    return "Enter a valid number!"


#
user_number = input('Enter your number: ')
print(day_of_week(user_number))
