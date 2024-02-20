from Task1 import Polygon

class Rectangle(Polygon):

    def __init__(self, side_A, side_B):
        self.side_A = side_A
        self.side_B = side_B
    
    def calculateSquare(self)-> None:
        '''
        Class's method for calculate rectangle square.
        Return - > None
        '''
        print(f'The squer of rectangle equel to {self.side_A * self.side_B}')
    