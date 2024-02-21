class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.info = f"{self.name}s age is {self.age}"
    def get_info(self):
        return self.info