class vegtable:
    ''' A general vegtable class '''

    def __init__(self, n, q):
        '''Intializes the vegtable'''
        self.name = n
        self.quantity = q





    def Sell(self):
        '''Sell value for Vegetable'''
        raise NotImplementedError("Please Implement")
        #This containts a check to make sure subclasses implement this.
        return None

