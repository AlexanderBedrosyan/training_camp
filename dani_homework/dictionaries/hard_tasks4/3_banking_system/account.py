# Account
# Атрибути: owner, private __balance
# Методи: deposit(amount), withdraw(amount) (с проверки за отрицателни стойности)
class Account:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.__balance = balance  # private атрибут

    def deposit(self, amount: float):
        # Добавя пари към акаунта.
        if amount <= 0:
            raise ValueError("Сумата за внасяне трябва да е положителна.")
        self.__balance += amount

    def withdraw(self, amount: float):
        # Тегли пари от акаунта, ако има достатъчно средства.
        if amount <= 0:
            raise ValueError("Сумата за теглене трябва да е положителна.")
        if amount > self.__balance:
            raise ValueError("Недостатъчна наличност по акаунта.")
        self.__balance -= amount

    def get_balance(self) -> float:
        # Връща текущия баланс.
        return self.__balance

    def __str__(self):
        return f"Account({self.owner}, balance={self.__balance:.2f})"



