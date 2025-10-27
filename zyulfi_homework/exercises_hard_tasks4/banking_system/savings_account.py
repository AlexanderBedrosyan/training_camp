# Атрибути: interest_rate
# Методи: apply_interest(years)

class SavingsAccount:
    def __init__(self, interest_rate=float, balance=float):
        self.interest_rate = interest_rate
        self.balance = balance

    def apply_interest(self, years=float):
        self.balance += self.balance * (self.interest_rate * years)

    def get_balance(self):
        return self.balance
