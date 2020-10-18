# Create a bank account program
#
#       That has two attributes:
#
#       - owner
#       - balance
#
#       and two methods:
#
#       - deposit
#       - withdraw
#
# As an added requitement, withdrawals may not exceed the available balance
#
# Instantiate your class, make several deposits and withdrawals
# and test to make sure the account can't be overdrawn.

class Account():
    '''
    Creates a bank account with an account balance.
    The owner and opening balance are specified by the
    user.
    Amounts can be withdrawn or deposited, but withdrawals
    can not exceed available balance.
    Assumes owner - a string
    and balance, a float.
    '''

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.amount = amount

    def __str__(self):
        return f'Account owner: {self.owner}\nAccount balance: {self.balance}'


print('Hello and welcome to the bank account')


client = input('Please enter the account holder: ')
print(f'Account holder: {client}')
opening_balance = input('Please enter the opening balance: ')
acct1 = Account(client, opening_balance)

print(acct1)
