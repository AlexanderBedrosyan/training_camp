# Account
# Атрибути: owner, private __balance
# Методи: deposit(amount), withdraw(amount) (с проверки за отрицателни стойности)

class Account:
    def __init__(self, owner=str):
        self.owner = owner
        self.__balance = 0

    def deposit(self, amount=float) -> None:
        if amount <= 0:
            raise ValueError("Error")
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance or amount <= 0:
            raise ValueError("Error")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


