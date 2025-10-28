# Discount
# Атрибут: percent
# Метод: calculate(amount) → връща сумата след намалението
class Discount:
    def __init__(self, percent: float):
        self.percent = percent  # процент намаление

    def calculate(self, amount: float) -> float:
        # Връща сумата след прилагане на намалението.
        if self.percent < 0 or self.percent > 100:
            raise ValueError("Discount percent must be between 0 and 100.")
        return amount * (1 - self.percent / 100)

    def __str__(self):
        return f"Discount({self.percent}%)"
