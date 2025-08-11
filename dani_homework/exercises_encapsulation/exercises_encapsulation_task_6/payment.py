# Mixin PaymentMixin с метод calculate_payment(rate)

class PaymentMixin:
    def calculate_payment(self, rate):
        return self._hours * rate

