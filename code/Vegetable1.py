import math
from vegtable import vegtable

class Vegetable1(vegtable):
    '''This is a fruit'''

    def __init__(self, n, q):
        '''Intializes the vegtable'''
        self.age = 1
        self.price = 3
        self.agefactor = 10
        self.pricefactor = 0
        self.location = 1
        vegtable.__init__(self,n, q)




    def Sell(self):
        '''The sellability factor of the Vegetable'''
        return self.agefactor+self.pricefactor



