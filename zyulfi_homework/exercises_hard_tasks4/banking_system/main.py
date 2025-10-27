from account import Account
from savings_account import SavingsAccount
from bank import Bank

a = Account("Gugov")

a.deposit(500)
print(a.get_balance())
a.withdraw(50)
print(a.get_balance())

s = SavingsAccount(0.10,50)
s.apply_interest(3)
print(s.balance)

b = Bank()
b.add_account(a)
b.add_account(s)
print(b.list_of_account)
print(b.total_assets())
print(b.richest_account())