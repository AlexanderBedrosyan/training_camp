# PremiumAccount (в premium_account.py) наследява Account,
# но има метод apply_bonus() – добавя 5% към баланса

from inheritance_mixims.Task_2_bank_system.account import Account

class PremiumAccount(Account):
    # def __init__(self, balance):
    #     Account.__init__(balance)

    def apply_bonus(self)->None:
        self._Account__balance *= 1.05

    def get_balance(self):
        return self._Account__balance
