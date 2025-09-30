#Portfolio: списък от Accounts и Investments; методи total_value(), projected_value(years)
from exercises_hard_tasks2.bank_portfolio.account import Account
from exercises_hard_tasks2.bank_portfolio.investment import Investment


class Portfolio:
    def __init__(self):
        self.list_of_accounts: list[Account] = []
        self.list_of_investments: list[Investment] = []

    def add_account(self, curr_account=object) -> None:
        self.list_of_accounts.append(curr_account)

    def add_investment(self, curr_investment=object) -> None:
        self.list_of_investments.append(curr_investment)

    def total_value(self) -> float:
        all_accounts = sum([curr_account.get_balance() for curr_account in self.list_of_accounts])
        all_investment = sum([curr_investment.get_investment() for curr_investment in self.list_of_investments])
        return all_accounts + all_investment

    def projected_value(self, years):
        all_accounts = sum([curr_account.get_balance() for curr_account in self.list_of_accounts])
        all_investment = sum([curr_investment.calculate_return(years) for curr_investment in self.list_of_investments])
        return all_accounts + all_investment


