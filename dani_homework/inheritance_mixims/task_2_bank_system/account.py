# Account (в account.py) има:
# private атрибут __balance
# методи deposit() и withdraw()

class Account:
    def __init__(self, balance=int):
        self.__balance = balance

    def deposit(self, amount=int)->None:
        self.__balance += amount

    def withdraw(self, amount=int)->None:
        self.__balance -= amount


