from account import Account
from customer import Customer
from bank import Bank

acc1 = Account()
acc1.deposit(500)
acc2 = Account()
acc2.deposit(300)

c = Customer("Maria")
c.add_account(acc1)
c.add_account(acc2)

bank = Bank("OBB")
bank.add_customer(c)

print(bank.total_assets())       # 800
print(bank.richest_customer().name)  # Maria
