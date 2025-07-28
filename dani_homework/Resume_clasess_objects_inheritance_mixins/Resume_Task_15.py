# Създай клас Account с атрибут balance.
# Добави метод deposit(amount) и метод withdraw(amount)
# (ако няма достатъчно средства, връща "Insufficient funds").
# Създай клас PremiumAccount, наследяващ Account,
# който override-ва withdraw(amount), за да позволява овърдрафт до -500.
# ---------------------------------------------------------------------

class Account:
    def __init__(self, balance=float):
        """
        Инициализира се акаунт с начално салдо.
        :param balance: (float) начално салдо
        """
        self.balance = balance

    def deposit(self, amount=float):
        """
        Депозира се сума в акаунта.
        :param amount:  (float) сумата за депозиране
        :return:        (str) потвърждава, връща текущ баланс
        """
        self.balance += amount
        return f"Deposited {amount}.\nNew balance: {self.balance}\n"

    def withdraw(self, amount=float):
        """
        Тегли се сума от акаунта.
        :param amount:  (float) сумата за теглене
        :return:        (str) ако има средства – потвърждава, връща нов баланс,
                        ако няма достатъчна наличност – "Insufficient funds"
        """
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrew {amount}.\nNew balance: {self.balance}\n"

class PremiumAccount(Account):
    def withdraw(self, amount=float):
        """
        Тегли се сума от акаунта, позволявайки овърдрафт до -500.
        :param amount:  (float) сумата за теглене
        :return:        (str) ако не надвишава овърдрафта – потвърждава, връща нов баланс,
                        връща – "Overdraft limit exceeded"
        """
        if self.balance - amount < -500:
            return "Overdraft limit exceeded"
        self.balance -= amount
        return f"Withdrew {amount}.\nNew balance: {self.balance}"

    # Тестване
a = Account(100)
print(a.deposit(50))     # Deposited 50. New balance: 150
print(a.withdraw(200))   # Insufficient funds
print(a.withdraw(100))   # Withdrew 100. New balance: 50

p = PremiumAccount(100)
print(p.withdraw(550))   # Withdrew 550. New balance: -450
print(p.withdraw(100))   # Overdraft limit exceeded
