# Задача 5: Сравнение на банкови сметки
# Клас BankAccount:
#   private __balance

# Имплементирайте:
# __gt__, __lt__, __eq__

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def __gt__(self, other):
        return self.__balance > other.__balance

    def __lt__(self, other):
        return self.__balance < other.__balance

    def __eq__(self, other):
        return self.__balance == other.__balance

# Пример:

a1 = BankAccount(1000)
a2 = BankAccount(1500)
print(a1 < a2)   # True
print(a1 == a2)  # False
print(a2 > a1)   # True
