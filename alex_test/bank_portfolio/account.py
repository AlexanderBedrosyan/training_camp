class Account:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            return
        self.__balance -= amount

    def return_balance(self):
        return self.__balance