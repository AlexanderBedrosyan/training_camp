# Задача 15
# Създай клас Account с атрибут balance. Добави метод deposit(amount) и метод withdraw(amount)
# (ако няма достатъчно средства, връща "Insufficient funds").
# Създай клас PremiumAccount, наследяващ Account, който override-ва withdraw(amount),
# за да позволява овърдрафт до -500.

class Account:
    def __init__(self, balance=float):
        self.balance = balance

    def deposit(self, amount=float) -> None:
        self.balance += amount

    def withdraw(self, amount=float) -> None:
        self.balance -= amount
        if self.balance <= 0:
            print(f"Insufficient funds")


class PremiumAccount(Account):
    def withdraw(self, amount=float) -> None:
        if self.balance - amount < -500:
            print("Оverdraft limit exceeded")
        self.balance -= amount
        print(f"current balance: {self.balance}")


current_account = Account(200)
print(current_account.balance)
current_account.deposit(40)
print(current_account.balance)
current_account.withdraw(250)

current_account2 = PremiumAccount(200)
current_account2.withdraw(400)
current_account2.withdraw(500)
current_account2.deposit(200)
print(current_account2.balance)

