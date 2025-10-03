# Customer (TransactionMixin)
# Атрибути: name, private __accounts
# Методи: add_account(), total_balance()
from oop_mixin_tasks.banking_app.account import Account
from oop_mixin_tasks.banking_app.transaction_mixin import TransactionMixin


class Customer(TransactionMixin):
    def __init__(self, name):
        self.name = name
        self.__accounts: list[Account] = []

    def add_account(self, curr_account) -> None:
        self.__accounts.append(curr_account)

    def total_balance(self):
        return sum([curr_acc.get_balance() for curr_acc in self.__accounts])
