from account import Account
from customer import Customer
from bank import Bank

a1 = Account("BG001")
a2 = Account("BG002")

c = Customer("Georgi")
c.add_account(a1)
c.add_account(a2)

a1.deposit(1000)
c.transfer(a1, a2, 400)

print(a1.get_balance())  # 600
print(a2.get_balance())  # 400

b = Bank()
b.add_customer(c)
print(b.find_customer("Georgi"))

c.transfer(a1, a2, 4000)
c.transfer(a1, a2, -4000)

a1.deposit(-200)
print(a1.withdraw(-4000))