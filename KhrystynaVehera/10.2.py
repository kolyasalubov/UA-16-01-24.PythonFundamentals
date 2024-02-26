class Human():

    def __init__(self, name):
        self.name = name
    
    def greeting(self):
        return f"Hello, {self.name}"
    
    @classmethod
    def homosapiens(self):
        return f"This is Homosapien species."

    @staticmethod
    def nice_dog():
        print("Homosapien`s pets like dogs are so nice.")



human = Human("Any")    

print(human.greeting())

print(Human.homosapiens())
Human.nice_dog()
    
   

