class Employee:
    count = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.count += 1
    def output_employee_info(self):
        return f"{self.name}'s salary is: {self.salary}"
    def counter(cls):
        return cls.count
    """The class for showing information about employees """

class information(Employee):
    
    def info():
        print(f"Base: {Employee.__base__}") 
        print(f"Namespace: {Employee.__dict__}")
        print(f"Name: {Employee.__name__}")
        print(f"Module: {Employee.__module__}") 
        print(f"Documentetion :{Employee.__doc__}") 

# creating subclass of "Employee"
person1 = Employee("Alexander",1000)

#outputting the result
print(person1.output_employee_info())
print(Employee.counter(Employee))
print(information.info())