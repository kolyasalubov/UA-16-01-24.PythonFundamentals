def get_day_of_week(number):
    days_of_week = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    if not isinstance(number, int):
        raise TypeError("Input must be a numerical value")
    if number < 1 or number > 7:
        raise ValueError("Invalid day")
    else:
        return days_of_week.get(number)


def main():
    try:
        number = input("Enter a number (1-7) representing a day of the week: ")
        result = get_day_of_week(number)
        print(f'The day of the week corresponding to {number} is {result}.')

    except (ValueError, TypeError) as e:
        print(e)

