days = ["Monday","Tuesday","Wednesday","Thirsday","Friday","Saturday","Sunday"]


while True:
    try:
        number = int(input("Enter the number or type q to quit the loop: "))
        print(f"The day is {days[number-1]}")
    except IndexError:
        print("Wrong number")
    except ValueError:
        print("Wrong symbol")
    finally:
        print("Has done")
