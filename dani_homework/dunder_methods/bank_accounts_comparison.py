class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private атрибут

    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return self.__balance == other.__balance
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, BankAccount):
            return self.__balance < other.__balance
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, BankAccount):
            return self.__balance > other.__balance
        return NotImplemented


# Примерно използване:
a1 = BankAccount(1000)
a2 = BankAccount(1500)

print(a1 < a2)   # True
print(a1 == a2)  # False
print(a2 > a1)   # True
