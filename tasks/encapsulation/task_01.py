# Създай клас Account, който има private атрибут __balance. Добави методи deposit(amount) и get_balance().

class Account:

    def __init__(self, balance=float):
        self.__balance = balance

    def deposit(self, amount=float) -> None:
        self.__balance += amount

    def get_balance(self) -> float:
        return self.__balance

current_account = Account(222)
current_account.deposit(20)
print(current_account.get_balance())