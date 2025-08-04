# Създай клас Account, който има private атрибут __balance.
# Добави методи deposit(amount) и get_balance().
# ----------------------------------------------------------

class Account:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance    # self атрибут за баланса

    def deposit(self, amount = bool):
        """
        Добавя сума към баланса, ако е положителна.
        :param amount: числова стойност
        :return: True ако е успешно, False ако сумата е невалидна
        """
        if amount > 0:
            self.__balance += amount
            return True
        else:
            return False

    def get_balance(self)-> float:
        """
        текущия баланс.
        """
        return self.__balance


#
acc = Account()
print(acc.get_balance())  # 0

acc.deposit(100)
print(acc.get_balance())    # 100

acc.deposit(-50)            # няма да промени баланса
print(acc.get_balance())    # отново 100
