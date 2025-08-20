from savings import SavingsAccount


acc = SavingsAccount(1000, 0.05)
acc.deposit(500)
acc.apply_interest()
print(acc.balance)
print(acc.get_logs())

