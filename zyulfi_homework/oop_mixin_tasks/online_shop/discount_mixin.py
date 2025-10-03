# apply_discount(price, percent)

class DiscountMixin:
    def apply_discount(self, price, persent):
        return price - ((price * persent) / 100)
