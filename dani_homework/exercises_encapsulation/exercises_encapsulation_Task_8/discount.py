# Mixin DiscountMixin с:
# class атрибут discount_rate = 0.1
# метод apply_discount()

class DiscountMixin:
    discount_rate = 0.1
    def apply_discount(self):
        return self._total * (1 - self.discount_rate)