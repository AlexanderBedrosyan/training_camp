# Клас BankAccount с:
# private атрибут __balance
# @property и @setter за balance:
# не позволява отрицателна стойност

class BankAccount:
    def __init__(self, balance=int):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError(f"Cannot be less than 0")
        self.__balance = value