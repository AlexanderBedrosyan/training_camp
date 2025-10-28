# SavingsAccount (Account)
# Атрибути: interest_rate
# Методи: apply_interest(years)
from account import Account

class SavingsAccount(Account):
    def __init__(self, owner: str, balance: float = 0.0, interest_rate: float = 0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate  # например 0.02 = 2%

    def apply_interest(self, years: int):
        # Добавя лихва върху баланса за определен брой години.
        if years <= 0:
            raise ValueError("Годините трябва да са положително число.")
        # формула за проста лихва
        interest = self.get_balance() * (self.interest_rate * years)
        self.deposit(interest)
        return interest

    def __str__(self):
        return f"SavingsAccount({self.owner}, balance={self.get_balance():.2f}, rate={self.interest_rate*100:.1f}%)"
