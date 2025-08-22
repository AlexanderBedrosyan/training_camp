from order import Order
from discount import DiscountMixin

class DiscountOrder(Order, DiscountMixin):
    pass
o = DiscountOrder()
o.add_item(100)
print(o.apply_discount())  # 90.0