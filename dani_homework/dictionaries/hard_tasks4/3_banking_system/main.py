from account import Account
from savings_account import SavingsAccount
from bank import Bank

# Създаваме акаунти
a1 = Account("Ivan", 500)
a2 = SavingsAccount("Maria", 1000, 0.05)

# Извършваме операции
a1.deposit(200)
a2.apply_interest(2)  # 2 години с 5% лихва

# Създаваме банка и добавяме акаунтите
b = Bank("MyBank")
b.add_account(a1)
b.add_account(a2)

# Проверяваме резултатите
print(a1)
print(a2)
print("Общо активи в банката:", b.total_assets())
print("Най-богат акаунт:", b.richest_account().owner)
