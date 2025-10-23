from credit_card import CreditCardPayment
from paypal import PayPalPayment
from bank_transfer import BankTransferPayment

payments = [
    CreditCardPayment(),
    PayPalPayment(),
    BankTransferPayment()
]

for p in payments:
    print(p.process(100))