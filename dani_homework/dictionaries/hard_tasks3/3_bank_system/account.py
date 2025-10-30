# Account
# Атрибути: private __balance
# Методи:
# deposit(amount)
# withdraw(amount) (с проверка за достатъчна наличност)
# get_balance()

class Account:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("The amount must be positive")

    def withdraw(self, amount:float):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("Not enough")

    def get_balance(self):
        return self.__balance



