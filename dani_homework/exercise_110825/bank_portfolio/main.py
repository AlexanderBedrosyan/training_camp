from account import Account
from Investment import Investment
from portfolio import Portfolio

a1 = Account(1000)
a2 = Account(2000)

inv1 = Investment(5000, 0.05)
inv2 = Investment(3000, 0.07)

portfolio = Portfolio()
portfolio.add_account(a1)
portfolio.add_account(a2)
portfolio.add_investment(inv1)
portfolio.add_investment(inv2)

print("Total value now:", portfolio.total_value())
print("Projected value in 5 years:", portfolio.projected_value(5))
