class Human:
    def __init__(self, name):
        self.name = name
    
    
    def greet(self):
        # print('Hello, nice to meet you')
        return 'Hello, nice to meet you'
        

    @classmethod
    def species(cls):
        return cls.__name__, 'Homosapiens'

    @staticmethod
    def arbitrary_message():
        return ('arbitrary message')
    

person = Human('Andrew')

print(person.name)
print(person.greet())
print(person.species())
print(person.arbitrary_message())