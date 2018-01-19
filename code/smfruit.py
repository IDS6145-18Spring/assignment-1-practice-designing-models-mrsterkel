class fruit:
    ''' A general fruit class '''

    def __init__(self, n, q):
        '''Intializes the fruit'''
        self.name = n
        self.quantity = q





    def Sell(self):
        '''Sell value for Fruit'''
        raise NotImplementedError("Please Implement")
        #This containts a check to make sure subclasses implement this.
        return None

