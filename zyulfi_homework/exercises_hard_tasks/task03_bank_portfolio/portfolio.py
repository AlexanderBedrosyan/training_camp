# Portfolio: държи списък от сметки и инвестиции, методи:
# total_value()
# projected_value(years) (събира текущите баланси + прогнозни печалби от инвестиции)
from account import Account
from investment import Investment

class Portfolio:
    def __init__(self):
        self.list_of_account: list[Account] = []
        self.list_of_investment: list[Investment] = []

    def add_account(self, curr_account=object) -> None:
        self.list_of_account.append(curr_account)

    def add_investment(self, curr_investment=object) -> None:
        self.list_of_investment.append(curr_investment)

    def total_value(self) -> float:
        return sum([curr_account.get_balance() for curr_account in self.list_of_account])

    def projected_value(self, years) -> float:
        all_investment = 0
        all_investment = sum([curr_investment.calculate_return(years) for curr_investment in self.list_of_investment])
        return all_investment + self.total_value()
