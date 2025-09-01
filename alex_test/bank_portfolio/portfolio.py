from typing import List
from account import Account
from investment import Investment

class Portfolio:

    def __init__(self):
        self.accounts: List[Account] = []
        self.investments: List[Investment] = []

    def add_account(self, current_account=object):
        self.accounts.append(current_account)

    def add_investment(self, current_investment:object):
        self.investments.append(current_investment)

    def total_amount_of_all_accounts(self):
        # total_amount_of_accounts = 0
        # for curr_account in self.accounts:
        #     total_amount_of_accounts += curr_account.return_balance() //// curr_account._Account__balance
        # return total_amount_of_accounts
        return sum([curr_account.return_balance() for curr_account in self.accounts]) # sum([1000, 2000]) => 3000

    def total_amount_of_all_investments(self):
        # total_amount_of_investments = 0
        # for inv in self.investments:
        #     total_amount_of_investments += inv.return_amount() //// inv._Investment__amount
        # return total_amount_of_investments
        return sum([curr_inv.return_amount() for curr_inv in self.investments])

    def total_value(self):
        return self.total_amount_of_all_accounts() + self.total_amount_of_all_investments()

    def sum_all_investments_by_year(self, years):
        # total_inv_returns = 0
        # for inv in self.investments:
        #     total_inv_returns += inv.calculate_returns(years)
        # return total_inv_returns
        return sum([inv.calculate_returns(years) for inv in self.investments])

    def projected_value(self, years):
        return self.total_amount_of_all_accounts() + self.sum_all_investments_by_year(years)


# print(portfolio.projected_value(2))   # (1000+2000)    +   5000*(1.05^2) = 8,512.5
                                        # total_balance      total_investments_value_for_year