def check(x):
    if x > 0:
        if x % 2 == 0:
            return "Your age is even"
        else:
            return "Your age is odd"
    else:
        try:
            if x == 0:
                raise Exception("You eneterned zero.")
            elif x < 0:
                raise Exception("You enterned negative number")
        except Exception as e:
            print(f"Problem: {e}")

try:
    age = int(input("Enter your age: "))
    print(check(age))
except ValueError:
    print("You did not entern  the number")