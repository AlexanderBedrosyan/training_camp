from premium_account import PremiumAccount

acc = PremiumAccount(1000)
acc.deposit(200)
acc.apply_bonus()
print(acc.get_balance())  # ~1260.0