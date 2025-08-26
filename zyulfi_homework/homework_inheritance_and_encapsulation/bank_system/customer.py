# Атрибути: name, private __accounts (списък от Account)
# Методи:
# add_account(account) → добавя сметка
# total_balance() → връща общата сума по сметки
# richest_account() → връща сметката с най-много пари
from account import Account

class Customer:
    def __init__(self, name=str):
        self.name = name
        self.__accounts: list[Account] = []

    def add_account(self, curr_account=object) -> None:
        self.__accounts.append(curr_account)

    def total_balance(self) -> int:
        all_sum_balance = 0
        for curr_account in self.__accounts:
            all_sum_balance += curr_account.get_balance()
        return all_sum_balance

    def richest_account(self) -> object:
        best_account = None
        best_balance = 0
        for curr_account in self.__accounts:
            if best_balance <= curr_account.get_balance():
                best_balance = curr_account.get_balance()
                best_account = curr_account
        return best_account

