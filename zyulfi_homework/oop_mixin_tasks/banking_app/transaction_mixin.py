# TransactionMixin
# Метод: transfer(from_acc, to_acc, amount)
from account import Account

class TransactionMixin:
    def transfer(self, from_acc=Account, to_acc=Account, amount=float or int):
        if from_acc.withdraw(amount):
            to_acc.deposit(amount)
        else:
            print("Error")

