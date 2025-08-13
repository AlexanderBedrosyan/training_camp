# Bank Example
# Създай клас BankAccount с атрибут balance и метод check_balance(),
# който връща текущия баланс.
# Създай клас SavingsAccount,
# който наследява BankAccount и има метод add_interest(rate),
# който увеличава баланса с процентното оскъпяване.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        # rate е в проценти: напр. 5 означава 5%
        interest = self.balance * (rate / 100)
        self.balance += interest


# Тест
account = SavingsAccount(1000)
print("Начален баланс:", account.check_balance())

account.add_interest(5)
print("Баланс след лихва:", account.check_balance())

