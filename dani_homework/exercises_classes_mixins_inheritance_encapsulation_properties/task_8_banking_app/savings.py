# SavingsAccount: добавя interest_rate, метод apply_interest()
from account import Account
from logger import LoggerMixin

class SavingsAccount(Account, LoggerMixin):
    def __init__(self, balance=float, interest_rate=float):
        Account.__init__(self, balance)
        LoggerMixin.__init__(self)
        self.interest_rate = interest_rate
        self.log(f" The account created with balance {balance} and interest rate {interest_rate}")

    def deposit(self, amount: float):
        super().deposit(amount)
        self.log(f"Deposited {amount}, new balance: {self.balance}")

    def withdraw(self, amount: float):
        super().withdraw(amount)
        self.log(f"Withdrew {amount}, new balance: {self.balance}")

    def apply_interest(self):
        interest = self.balance * self.interest_rate # как се образува лихвата???
        self.balance += interest
        self.log(f"Applied interest {interest}, new balance: {self.balance}")