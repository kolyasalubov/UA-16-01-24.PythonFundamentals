class Human():
    def __init__(self,name):
        self.name = name

    @classmethod
    def species(cls):
        print("This is the species of Homosapiens")

    @staticmethod
    def massage():
        print("Hello human")


Human1 = Human('John')
Human.massage()
Human.species()