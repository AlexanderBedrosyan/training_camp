# CreditCardPayment: наследява Payment,
# метод process() → "Processing credit card payment of {amount}"
from exercises_polymorphism.payment_system.payment import Payment

class CreditCardPayment(Payment):
    def process(self, amount):
        return f"Processing credit card payment of {amount}"