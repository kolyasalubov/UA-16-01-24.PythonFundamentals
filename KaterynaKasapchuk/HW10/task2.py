class Human():
    def __init__(self, name):
        self.name = name

    def greet_human(self):
        print(f"Hello {self.name}!")

    @classmethod
    def say_info(cls):
        return "I am a 'Homosapiens'"
    @staticmethod
    def bye():
        print("Bye bye!")

