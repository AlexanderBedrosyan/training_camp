# Атрибути: списък от акаунти
# Методи: total_assets(), richest_account()
from account import Account


class Bank:
    def __init__(self):
        self.list_of_account: list[Account] = []

    def add_account(self, curr_account:object):
        if curr_account.__class__.__name__ in ("Account", "SavingsAccount"):
            self.list_of_account.append(curr_account)

    def total_assets(self):
        return sum([curr_account.get_balance() for curr_account in self.list_of_account])

    def richest_account(self):
        best_account = None
        best_balance = 0
        for curr_account in self.list_of_account:
            if curr_account.get_balance() >= best_balance:
                best_balance = curr_account.get_balance()
                best_account = curr_account
        return best_account.get_balance()