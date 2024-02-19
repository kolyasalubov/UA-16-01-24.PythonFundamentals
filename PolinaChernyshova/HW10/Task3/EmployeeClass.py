
class Employee():
    '''
    Employee - A class for storing and recording information about employees. 
    It has attributes: name, salary and a class attribute _amount_of_employee
    for amount of employees
    Has instance method printInformation()
    class method printAmount()
    getters and setters for name amd salary
    '''
    
    _amount_of_employee = 0

    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
        Employee._amount_of_employee += 1
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, salary):
        self._salary = salary

    
    def printInformation(self):
        '''
        Instance method printInformation()
        Print information about employee (name and salary)
        Return -> None
        '''
        print(f'Name: {self._name}. Salary: {self._salary}')
    
    
    @classmethod
    def printAmount(cls):
        '''
        Class method printAmount()
        Print information about amount of employee
        Return -> None
        '''
        print(f'Amount of employee eaqvel to {cls._amount_of_employee}')
