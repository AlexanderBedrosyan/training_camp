from discounted_item import DiscountedItem

i = DiscountedItem("Chair", 100)
i.apply_discount(10)
print(i.price)  # 90.0