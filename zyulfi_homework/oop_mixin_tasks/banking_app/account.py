# Account
# Атрибути: iban, private __balance=0
# Методи: deposit(amount), withdraw(amount), get_balance()

class Account:
    def __init__(self, iban):
        self.iban = iban
        self.__balance = 0

    def deposit(self, curr_amount) -> None:
        if curr_amount >= 0:
            self.__balance += curr_amount
            return True
        else:
            print("Error")
            return False

    def withdraw(self, curr_amount) -> None:
        if 0 < curr_amount <= self.__balance:
            self.__balance -= curr_amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        return self.__balance

