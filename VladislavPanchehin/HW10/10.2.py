class Human:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def introduce(self):
        print(f"Hello! My name is {self.name}, I am old {self.age}, and I'm a man {self.gender}")
    #  Create a class method in class
    @classmethod
    def greeting_info(cls):
        return f"This is a member of the Homo sapiens species 'Class name - {cls.__name__}'"
    # Create class static method
    @staticmethod
    def greetings_user():
        return "Burn,Baby, Burn!"
        
# Create class object Human
person_one = Human("Vladislav",30,"man")
#run method
person_one.introduce()
#  Calling a method class
print(Human.greeting_info())
# Calling a static method
print(Human.greetings_user())