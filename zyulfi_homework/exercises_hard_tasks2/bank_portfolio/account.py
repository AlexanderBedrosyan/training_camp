#private __balance; методи deposit(), withdraw()

class Account:
    def __init__(self, amount=float):
        self.__balance = amount

    def deposit(self, amount=float) -> None:
        self.__balance += amount

    def withdraw(self, amount=float) -> None:
        if amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance