# Account
# Атрибути: owner, private __balance
# Методи: deposit(amount), withdraw(amount) (с проверки за отрицателни стойности)

class Account:
    def __init__(self, owner:str):
        self.owner = owner
        self.__balance = 0

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("The amount cannot be negative")

        self.balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("The amount cannot be more than balance")

        self.__balance -= amount


