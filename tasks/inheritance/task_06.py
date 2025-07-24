# ✅ Задача 6 – Bank Example Създай клас BankAccount с атрибут balance и метод check_balance(), който връща текущия
# баланс. Създай клас SavingsAccount, който наследява BankAccount и има метод add_interest(rate), който увеличава
# баланса с процентното оскъпяване.

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        print(f"Current amount in our bank: {self.balance}")

class SavingsAccount(BankAccount):

    def add_interest(self, rate):
        self.balance += (self.balance * (rate / 100))

current_account = SavingsAccount(20)
current_account.check_balance()
current_account.add_interest(50)
current_account.check_balance()
current_account.add_interest(25)
current_account.check_balance()