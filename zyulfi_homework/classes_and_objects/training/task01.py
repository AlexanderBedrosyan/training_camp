# Задача 1.
# Създай клас Account, който има private атрибут __balance. Добави методи deposit(amount) и get_balance().

class Account:
    def __init__(self, balance=float):
        self.__balance = balance

    def deposit(self, amount=float) -> None:
        self.__balance += amount

    def get_balance(self) -> float:
        return self.__balance

current_balance = Account(250)
print(current_balance.get_balance())
current_balance.deposit(50)
print(current_balance.get_balance())
