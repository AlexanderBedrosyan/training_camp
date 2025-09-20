# Investment: private __amount, rate, метод calculate_return(years)

class Investment:
    def __init__(self, amount, rate):
        self.__amount = amount
        self.rate = rate

    def calculate_return(self, years):
        return self.__amount * (1 + years * self.rate )

