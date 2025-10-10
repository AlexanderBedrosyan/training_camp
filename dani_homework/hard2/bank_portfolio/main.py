from account import Account
from investment import Investment
from portfolio import Portfolio

acc1 = Account(1000)
acc2 = Account(2000)
inv = Investment(5000, 0.05)

# print(acc1)
# print(acc2)

portfolio = Portfolio()
portfolio.add_account(acc1)
portfolio.add_account(acc2)
portfolio.add_investment(inv)

print(portfolio.total_value())         # 8000
print(portfolio.projected_value(2))   # 1000+2000 + 5000*(1.05^2)