#Account: private __balance; методи deposit(), withdraw()
import self


class Account:
    def __init__(self, balance: float = 0.0) -> None:
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.__balance = float(balance)

    @property
    def balance(self) -> float:
        return self.__balance  # показва текущия баланс


    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount

    def __str__(self) -> str:
        return f"Account(balance={self.__balance:.2f})"



#test
a=Account(150)
a.deposit(20)
a.withdraw(65)
