# Атрибути: private __balance
# Методи:
# deposit(amount) → увеличава баланса
# withdraw(amount) → намалява баланса (само ако има достатъчно средства)
# get_balance() → връща текущия баланс

class Account:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount=int) -> None:
        self.__balance += amount

    def withdraw(self, amount=int) -> None:
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Error")

    def get_balance(self) -> int:
        return self.__balance


