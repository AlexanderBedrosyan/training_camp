# Създай PayrollEmployee(Employee, PaymentMixin, LoggerMixin)

from payment import PaymentMixin
from log import LoggerMixin
from employee import Employee

class PayrollEmployee(Employee, PaymentMixin, LoggerMixin):
    pass

e = PayrollEmployee("Ivan")
e.work(10)
print(e.calculate_payment(20))  # 200
e.log("Payment calculated.")    # LOG: Payment calculated.