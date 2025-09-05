from account import Account
from customer import Customer
from bank import Bank

a1 = Account()
c1 = Customer("Maria", a1)

c1.deposit(500)
c1.withdraw(200)

b = Bank()
b.add_customer(c1)

print(c1.balance())    # 300
print(b.total_assets()) # 300