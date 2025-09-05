# Атрибути: name, private __accounts (списък от Account)
# Методи:
    # add_account(account)   → добавя сметка
    # total_balance()        → връща общата сума по сметки
    # richest_account()      → връща сметката с най-много пари
#---------------------------------------------------------------
from account import Account


class Customer:
    def __init__(self, name:str):
        self.name = name
        self.__accounts: list[Account] = []

    def add_account(self, curr_account):
        self.__accounts.append(curr_account)

    def total_balance(self):
        t_balance = 0
        curr_account = 0
        for curr_account in self.__accounts:
            t_balance += curr_account.get_balance()
        return t_balance

    def richest_account(self):
        curr_amount_account = 0
        richest_account = None

        for curr_account in self.__accounts:
            if curr_amount_account <= curr_account.get_balance():
                curr_amount_account = curr_account.get_balance()
                richest_account = curr_account

        return richest_account




