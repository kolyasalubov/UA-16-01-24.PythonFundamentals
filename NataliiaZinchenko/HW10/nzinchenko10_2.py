# Creating class Human with: name property, welcome message method, class method about specie information and static method 
# with arbitrary information

class Human:
    '''
    Class Human contains information about name and age of objects
    '''
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def say_hi(self):
        '''
        say_hi() method returns personalized greeting
        '''
        return f"Hi, {self.name}!"
    

    def say_age(self):
        '''
        say_age() returns personalized message about class object's age
        '''
        return f"{self.name} is {self.age} years old"


    @classmethod
    def specie(cls):
        '''
        class method specie() returns message about object's specie
        '''
        return "This is Homosapiens specie"
    

    @staticmethod
    def arbitrary_message():
        '''
        static method arbitrary_message() returns an arbitrary message
        '''
        return "Static method is called"
    

# testing
person_1 = Human("Erik", 20)
person_2 = Human("Melissa", 35)
print(person_1.say_hi())
print(person_1.say_age())
print(person_2.say_hi())
print(person_2.say_age())
