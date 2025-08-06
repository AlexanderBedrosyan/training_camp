# Задача 4: Създай Mixin клас LogMixin с метод log(message), който принтира: [LOG]: {message}.

class LogMixin:

    def log(self, message):
        print(f"[LOG]: {message}")

# 🔹 Задача 6
# Създай Mixin DriveMixin с метод drive() връщащ "Driving...".

class DriveMixin:

    def drive(self):
        return "Driving..."


# Задача 11
# Създай два Mixin класа:
#
# PaymentMixin с метод pay(amount) връщащ "Paid {amount} USD"
# DiscountMixin с метод apply_discount(price, discount), връщащ цената след намаление

class PaymentMixin:

    def pay(self, amount=int) -> str:
        return f"Paid {amount} USD"

class DiscountMixin:

    def apply_discount(self, price=float, discount=float) -> float:
        return price * (1 - discount / 100)

# 🔹 Задача 12
class MailCheckerMixin:

    def is_valid_mail(self, email):
        if "@" in email:
            return True
        print("Wrong email!")
        return False
