# DiscountMixin: метод apply_discount(%)
class DiscountMixin:
    def __init__(self):
        self._discount = []

    def apply_discount(self, price, rate):
        if not (0 <= rate <= 1):
            raise ValueError("Discount rate must be between 0 and 1")
        discounted_price = price * (1 - rate)
        self._discount.append((price, rate, discounted_price))
        return discounted_price
