# BankTransferPayment: наследява Payment,
# метод process() → "Processing bank transfer of {amount}"
from exercises_polymorphism.payment_system.payment import Payment


class BankTransferPayment(Payment):
    def process(self, amount):
        return f"Processing bank transfer of {amount}"