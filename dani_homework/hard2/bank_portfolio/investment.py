#Investment: private __amount, rate; метод calculate_return(years)
import math


class Investment:
    def __init__(self, amount: float, rate: float):
        self.__amount = amount
        self.rate = rate


    @property
    def amount(self)-> float:
        return self.__amount

# Сложната лихва се изчислява въз основа на главницата, лихвения процент (ГПР или годишен процент) и необходимото време:
# P  е главницата (първоначалната сума, която заемате или депозирате)
# r  е годишният лихвен процент (процент)
# n  е броят години, за които сумата е депозирана или заета.
# A  е сумата пари, натрупана след n години, включително лихвите.
# A = P * (1 + r) ** n

    def calculate_return(self, years:int)-> float:
        calc_return = 0
        if years < 0:
            raise ValueError("the years cannot be negative")
        calc_return = self.__amount * math.pow(1.0 + self.rate, years)
        return calc_return

    def __str__(self)-> str:
        percentage = self.rate * 100
        return f"Investment (amount={self.__amount:.2f}, rate={percentage:.2f}%)"


