# Атрибути: name, account
# Методи:
# deposit(amount) → подава към акаунта
# withdraw(amount)
# balance()
from account import Account


class Customer:
    def __init__(self, name, account:Account):
        self.name = name
        self.account = account

    def deposit(self, amount) -> None:
        self.account.deposit(amount)

    def withdraw(self, amount) -> None:
        self.account.withdraw(amount)

    def balance(self) -> float or int:
        return self.account.get_balance()


