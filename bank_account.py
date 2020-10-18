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
# Instantiate your class, make several deposits and withdrawals, and test to make
# sure the account can't be overdrawn.

class Account():

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.ammount = amount

    def __str__(self):
        a=f'Account owner: {self.owner}\n'
        b=f'Account balance: {self.balance}'
        return a+b
acct1 = Account('Adam',100)
print(acct1)
