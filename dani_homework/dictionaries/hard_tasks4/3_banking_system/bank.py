# Bank
# Атрибути: списък от акаунти
# Методи: total_assets(), richest_account()
from account import Account
from savings_account import SavingsAccount

class Bank:
    def __init__(self, name: str):
        self.name = name
        self.accounts = []  # списък от акаунти (Account или SavingsAccount)

    def add_account(self, account: Account):
        # Добавя акаунт към банката.
        self.accounts.append(account)

    def total_assets(self) -> float:
        # Връща общата сума на всички средства в банката.
        return sum(acc.get_balance() for acc in self.accounts)

    def richest_account(self) -> Account:
        # Връща акаунта с най-голям баланс.
        if not self.accounts:
            return None
        return max(self.accounts, key=lambda a: a.get_balance())

    def __str__(self):
        return f"Bank({self.name}, accounts={len(self.accounts)})"
