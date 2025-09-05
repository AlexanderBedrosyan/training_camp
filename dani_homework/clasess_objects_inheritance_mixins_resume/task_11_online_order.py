# Създай два Mixin класа:
# PaymentMixin с метод pay(amount) връщащ "Paid {amount} USD"
# DiscountMixin с метод apply_discount(price, discount), връщащ цената след намаление
# Създай клас OnlineOrder, който използва и двата mixin-а и има атрибут order_id.
# # Тествай pay и apply_discount.
#---------------------------------------------------------------------------------

class PaymentMixin:
    def pay(self, amount: float)-> str:
        return f"Paid {amount} USD"


class DiscountMixin:
    def apply_discount(self, price: float, discount: float)->float:
        return price * (1 - discount / 100)


class OnlineOrder(PaymentMixin, DiscountMixin):
    def __init__(self, order_id: int)->None:
        self.order_id = order_id

oo = OnlineOrder(123)

print(oo.pay(50))
print(oo.apply_discount(100, 5))
