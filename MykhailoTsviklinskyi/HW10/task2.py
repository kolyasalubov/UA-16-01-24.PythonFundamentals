class Human:
    # instance attributes
    def __init__(self, name):
        self.name = name

    # instance method
    def hello_each_person(self):
        return f"Welcome, {self.name}"
    
    @classmethod
    def return_species(cls):
        return 'Human a species of "Homosapiens"', cls

    @staticmethod
    def test_func():
        return "Test message"

person1 = Human('Misha')
person2 = Human('Yana')

# instance methods
print(person1.hello_each_person())
print(person2.hello_each_person())

# class methods
print(Human.return_species())
print(person1.return_species())
print(person2.return_species())

# static methods
print(person1.test_func())
print(person2.test_func())
