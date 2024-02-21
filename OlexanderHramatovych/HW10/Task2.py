
class Human:
# class of human
    def __init__(self,name):
        self.name = name
    def hello(self):
        return f"Hello {self.name}"
    def species(self):
        species = "Homosapiens"
        return f"{self.name} is {species}"
    

# subclasses
person1 = Human("Alexander")
person2 = Human("Dmytro")
 
 #outputting the result
print(person1.hello())
print(person2.hello())
print(person1.species())    
print(person2.species())
