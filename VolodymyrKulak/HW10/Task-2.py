
class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f"Hello, {self.name}! Welcome here."

    @classmethod
    def species_info(cls):
        return f"I am a species of 'Homosapiens'"

    @staticmethod
    def arbit_message():
        return "This is the arbitrary message"


person1 = Human("Alice")
print(person1.welcome_message())

print(Human.species_info())
print(Human.arbit_message())
