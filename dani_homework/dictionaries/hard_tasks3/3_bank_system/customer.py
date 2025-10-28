# Customer
# Атрибути: name, account
# Методи: deposit(amount) → подава към акаунта
# withdraw(amount)
# balance()
from account import Account


class Customer:
    def __init__(self, name:str, account:Account):
        self.name = name
        self.account = account

    def deposit(self, amount):
        self.account.deposit(amount)

    def withdraw(self, amount):
        self.account.withdraw(amount)

    def balance(self):
        return self.account.get_balance()