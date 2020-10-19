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
        self.balance = self.balance + self.amount
        return self.balance
    
    def withdraw(self, debit):
        self.debit = debit
        self.balance = self.balance - self.debit
        return self.balance
    
    def __str__(self):
        return f'Account owner: {self.owner}\nAccount balance: {self.balance}'


print('Hello and welcome to the bank account')
client = input('Please enter the account holder: ')
print(f'Account holder: {client}')
opening_balance = float(input('Please enter the opening balance: '))
acct1 = Account(client, opening_balance)
print(acct1)
transaction = input('Please type, d for deposit, w for withdraw, \
or b for account balance: ')
if transaction == 'd':
    new_deposit = float(input('Please enter an amount to deposit: '))
    acct1.deposit(new_deposit)
    print(acct1)
elif transaction == 'w':
    invalid_debit = True    
    new_withdawal = float(input('Please enter an amount to withdraw: '))
    while invalid_debit:
        if new_withdawal > acct1.balance:
            new_withdawal = float(input(f'Withdawal exceeds current account balance, {acct1.balance}. \n\
Please enter another amount: '))
        else:
            acct1.withdraw(new_withdawal)
            invalid_debit = False
            print(acct1)
elif transaction == 'b':
    print(acct1.balance)
