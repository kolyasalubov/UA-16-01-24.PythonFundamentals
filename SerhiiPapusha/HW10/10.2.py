class Human:
    species = "Homosapiens"
    def __init__(self, name):
        self.name = name

    def welcome_msg(self):
        print(f"Welcome to 'Human' class, {self.name}")
    
    @classmethod
    def showInfo(cls):
        return cls.species
    
    @staticmethod
    def arbitraryMsg():
        return "arbitrary message."
    
hum1 = Human("Laila")
hum1.welcome_msg()
print(hum1.showInfo())
print(hum1.arbitraryMsg())