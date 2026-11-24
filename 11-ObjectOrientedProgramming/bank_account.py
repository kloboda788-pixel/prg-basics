###
# Module with a class describing a bank account
#
# Object: bank account
# States (fields):     account number, balance
# Behaviors (methods): deposit money, withdraw money, display information
#
class BankAccount:
    # the account number is given when the account is created
    def __init__(self, number):
        self.number = number
        self.balance = 0.0         # the initial balance is PLN 0

    # Deposits any amount on the account
    def deposit(self, amount):
        self.balance += amount

    # Withdraws the amount only if it does not exceed the balance
    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds on the account')
        else:
            self.balance -= amount

    # Displays the account number and balance (with a decimal comma)
    def display(self):
        # :.2f - two decimal places; replace() changes the dot into a comma
        balance = f'{self.balance:.2f}'.replace('.', ',')
        print(f'Bank Account No: {self.number}')
        print(f'Balance: PLN {balance}')
        print()