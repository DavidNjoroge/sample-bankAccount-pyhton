class Account:
    '''
    class that generates an instance of a bank acccount
    '''
    def __init__(self,first_name,last_name,):
        self.first_name=first_name
        self.last_name=last_name
        self.balance=0

    def check_balance(self):
        '''
        returns the curent balance
        '''
        return self.balance

    def deposit(self,amount):
        '''
        method that deposits to the balance
        args:
            amount: the amount to deposit
        '''
        self.balance += amount
