import unittest
from bank_account import Account

class TestCustomer(unittest.TestCase):
    '''
    class to test the functionality of the customer class
    '''

    def setUp(self):
        '''
        setup method to run before each test
        '''
        self.new_customer=Account('john','doe')

    def test_init(self):
        '''
        test case to test if the object is initialized correctly
        '''

        self.assertEqual(self.new_customer.first_name,"john")
        self.assertEqual(self.new_customer.last_name,"doe")
        self.assertEqual(self.new_customer.balance,0)

    def test_check_balance(self):
        '''
        test case to test a method that returns the balance
        '''
        self.assertEqual(self.new_customer.check_balance(),0)

    def test_deposit(self):
        '''
        test case to test if you can deposit
        '''
        self.new_customer.deposit(1000)
        self.assertEqual(self.new_customer.check_balance(),1000)

    # def test_withdraw(self):
    #     '''
    #     test case to test if you can withdraw from the balance
    #     '''
    #     self.new_customer.deposit(1000)
    #     self.new_customer.withdraw(400)
    #     self.assertEqual(self.new_customer.check_balance(),600)
    #
    # def test_withdraw2(self):
    #     '''
    #     test case to test if you withdraw more than the balance it returns a message
    #     '''
    #     self.new_customer.deposit(1000)
    #     self.new_customer.withdraw(1200)
    #     self.assertEqual(self.new_customer.withdraw(),False)
    #
if __name__ == '__main__':
    unittest.main()
