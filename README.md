## create an app that a customer
*  can create an account with an initial balance of zero
* as a customer i need to deposit cash
* as a customer i need to be able to withdraw
* as a customer i need to check my current balance

#### further exploration
* make an executable file
* the app should be able to create multiple accounts
* should be able to transfer cash from one account to the next

## instructions

* using the class customer make an methods according to the tests
* make sure all the tests pass.
* to run the tests in he terminal cd into the folder and run `$ python3 customer_test.py`

#### test cases(TDD)
* first test: test to see if the customer is initialized with the correct properties
* second test: test to see if you can check your balance
* test case: should be able to deposit an amount
* test case: should be able to withdraw from the account and if the amount withdrawed is more than the balance, should return message"you dont have enough cash to withdraw"
