# Задача 11
# Създай два Mixin класа:
#
# PaymentMixin с метод pay(amount) връщащ "Paid {amount} USD"
# DiscountMixin с метод apply_discount(price, discount), връщащ цената след намаление

# Създай клас OnlineOrder, който използва и двата mixin-а и има атрибут order_id. Тествай pay и apply_discount.
from mixins import PaymentMixin, DiscountMixin

class OnlineOrder(PaymentMixin, DiscountMixin):

    def __init__(self, order_id=int):
        self.order_id = order_id

our_order = OnlineOrder(123)
amount = 20
discount = 10
amount_after_discount = our_order.apply_discount(amount, discount)
print(our_order.pay(amount_after_discount))
print(our_order.order_id)
