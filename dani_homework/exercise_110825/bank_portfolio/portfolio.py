# Portfolio: държи списък от сметки и инвестиции,
# методи:
# total_value()
# projected_value(years) (събира текущите баланси + прогнозни печалби от инвестиции)

class Portfolio:
    def __init__(self):
        self.account_list = []
        self.inv_list = []

    def add_account(self, current_account):
        self.account_list.append(current_account)

    def add_investment(self, current_inv):
        self.inv_list.append(current_inv)

    def total_value(self):
        total_balance = 0
        for account in self.account_list:
            total_balance += account._Account__balance
        for inv in self.inv_list:
            total_balance += inv._Investment__amount

        return total_balance

    def projected_value(self, years):
        total_balance = 0
        for inv in self.inv_list:
            total_balance += inv.calculate_return(years)

        return total_balance