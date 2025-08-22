# Account с balance, deposit(), withdraw()

class Account:
    def __init__(self, balance=int or float):
        self.balance = balance

    def deposit(self, amount=float):
        if amount <= 0:
            raise ValueError("The deposit amount must be +")
        self.balance += amount

    def withdraw(self, amount=float):
        if amount <= 0:
            raise ValueError("The withdrawal amount must be + ")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
