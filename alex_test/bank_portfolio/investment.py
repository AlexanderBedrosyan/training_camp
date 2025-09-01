class Investment:

    def __init__(self, amount, rate):
        self.__amount = amount
        self.rate = rate

    def calculate_returns(self, years):
        return self.__amount * ((1 + self.rate) ** years) # not sure, may need checks in the end of the app

    def return_amount(self):
        return self.__amount
