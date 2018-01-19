import math
from fruit import fruit


class Fruit1(fruit):
    '''This is a fruit'''

    def __init__(self, n, q):
        '''Intializes the fruit'''
        self.age = 2
        self.price = 4
        self.agefactor = 9
        self.pricefactor = 0
        self.location = 1
        vegtable.__init__(self, n, q)

    def Sell(self):
        '''The sellability factor of the Fruit'''
        return self.agefactor + self.pricefactor



