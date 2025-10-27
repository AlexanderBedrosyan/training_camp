# PayPalPayment: наследява Payment,
# метод process() → "Processing PayPal payment of {amount}"
from exercises_polymorphism.payment_system.payment import Payment


class PayPalPayment(Payment):
    def process(self, amount):
        return f"Processing PayPal payment of {amount}"
