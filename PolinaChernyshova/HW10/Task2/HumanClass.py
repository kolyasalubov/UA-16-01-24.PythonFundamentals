
class Human():
    _kind = "Homosapiens"

    def __init__(self, name = "Human"):
        self.name = name
    
    def welcomeToHuman(self):
        print(f'Welcome, {self.name}')

    @classmethod
    def returnKind(cls):
        return cls._kind
    
    @staticmethod
    def returnSomeString():
        return 'City of stars \nAre you shining just for me?'

