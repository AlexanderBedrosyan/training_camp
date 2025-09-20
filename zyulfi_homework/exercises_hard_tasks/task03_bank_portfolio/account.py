# Account: private __balance, методи deposit(), withdraw()

class Account:
    def __init__(self, balance=float):
        self.__balance = balance

    def deposit(self, amount=float) -> None:
        self.__balance += amount

    def withdraw(self, amount=float) -> None:
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient availability")

    def get_balance(self) -> float:
        return self.__balance

