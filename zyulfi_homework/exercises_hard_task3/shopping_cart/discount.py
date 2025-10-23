# Атрибут: percent
# Метод: calculate(amount) → връща сумата след намалението

class Discount:
    def __init__(self, percent):
        self.percent = percent / 100

    def calculate(self, amount):
        return amount * (1 - self.percent)


