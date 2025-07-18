# Създай клас BankAccount с атрибут balance. Добави методи за deposit(amount) и withdraw(amount), които променят баланса.
# Добави и метод check_balance(), който връща текущия баланс.

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def is_balance_enough(self):
        return self.balance >= 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Add money in your bank - {amount}")
        print(self.check_balance())

    def withdraw(self, amount):
        self.balance -= amount

        if not self.is_balance_enough():
            self.balance += amount
            print(f"We cannot withdraw with {amount}. Your balance is {self.balance}. Needs more money in the bank.")
            print(self.check_balance())
        else:
            print(f"Withdraw your card balance with {amount}")
            print(self.check_balance())

    def check_balance(self):
        return f"Your balance is {self.balance}"


my_bank_account = BankAccount(20)
my_bank_account.withdraw(30)
my_bank_account.deposit(20)
my_bank_account.withdraw(30)
