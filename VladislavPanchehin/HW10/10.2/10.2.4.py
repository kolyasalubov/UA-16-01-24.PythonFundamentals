# Create class Person

class Person():
    # Determine the method

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f"{name}s age is {age}"

# Displaying information
    def display(self):
        return self.info


# Tested
person_one = Person('Vladik', 30)
print(person_one.display())
