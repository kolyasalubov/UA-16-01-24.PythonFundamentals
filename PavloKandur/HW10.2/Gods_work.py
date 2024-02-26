def God():
    list_of_humans = []
    man = Man("Adam")
    woman = Woman("Eve")
    list_of_humans.append(man)
    list_of_humans.append(woman)
    return list_of_humans

class Human():
    def __init__(self,name):
        self.name = name
        
class Man(Human):
    def __init__(self,name):
        super().__init__(name)
        
class Woman(Human):
    def __init__(self,name):
        super().__init__(name)