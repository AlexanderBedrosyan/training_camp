# Създай клас Marketplace, който управлява продукти и наличности.
# Условия:
# Речник {продукт: {"quantity": бр, "price": цена}}
# Метод add_product(name, quantity, price)
# Метод buy_product(name, count) – намаля количеството, ако има.
# Метод total_value() – връща общата стойност на всички стоки.


class Marketplace:
    def __init__(self):
        self.product = {}

    def add_product(self, name, quantity, price):
        self.product[name] = {}
        self.product[name]["quantity"] = quantity
        self.product[name]["price"] = price

    def buy_product(self, name, count):
        try:
            if self.product[name]["quantity"] >= count:
                self.product[name]["quantity"] -= count
        except KeyError:
            print(f"{name} is missing")

    def total_value(self):
        sum_value = 0
        for curr_key, curr_value in self.product.items():
            sum_value += curr_value["quantity"] * curr_value["price"]
        return sum_value


# Тест:
m = Marketplace()
m.add_product("Apple", 10, 2)
m.add_product("Banana", 5, 3)
m.buy_product("Apple", 3)
m.buy_product("Cerry", 5)
print(m.total_value())  # 29