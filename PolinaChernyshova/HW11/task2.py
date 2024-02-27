class CheckNumberError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


def get_day_by_number():
    try:
        user_number = int(input("Enter the number of week day: "))
        if user_number < 1 or user_number > 7:
            raise CheckNumberError(
                "Error: Your number cannot be less than 1 or greater than 7"
            )
        match user_number:
            case 1:
                print("Monday")
            case 2:
                print("Tuesday")
            case 3:
                print("Wensday")
            case 4:
                print("Thursday")
            case 5:
                print("Friday")
            case 6:
                print("Saturday")
            case 7:
                print("Sundey")
    except CheckNumberError as e:
        print(e.data)
    except ValueError:
        print(f"The number cannot be string")


get_day_by_number()
