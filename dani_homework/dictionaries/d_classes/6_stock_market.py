# Създай клас Marketplace, който управлява продукти и наличности.
# Условия: Речник {продукт: {"quantity": бр, "price": цена}}
# Метод add_product(name, quantity, price)
# Метод buy_product(name, count) – намаля количеството, ако има.
# Метод total_value() – връща общата стойност на всички стоки.
class Marketplace:
    def __init__(self):
# Структура: {продукт: {"quantity": бр, "price": цена}}
        self.products = {}

    def add_product(self, name: str, quantity: int, price: float):
# Добавя нов продукт или увеличава количеството му.
        if quantity < 0 or price < 0:
            raise ValueError("Количеството и цената трябва да са положителни.")
        if name not in self.products:
            self.products[name] = {"quantity": quantity, "price": price}
        else:
# ако вече съществува — увеличаваме количеството, обновяваме цената
            self.products[name]["quantity"] += quantity
            self.products[name]["price"] = price  # актуализира последната цена

    def buy_product(self, name: str, count: int):
# Намалява количеството, ако има достатъчно наличност.
        if name not in self.products:
            print(f"Продуктът '{name}' не съществува!")
            return
        if count <= 0:
            print("Количеството за покупка трябва да е положително!")
            return
        if self.products[name]["quantity"] < count:
            print(f"Недостатъчно количество от '{name}'!")
            return
        self.products[name]["quantity"] -= count

    def total_value(self) -> float:
# Връща общата стойност на всички налични стоки.
        return sum(info["quantity"] * info["price"] for info in self.products.values())

    def __str__(self):
        return f"Marketplace({len(self.products)} products)"

# Тест:
m = Marketplace()
m.add_product("Apple", 10, 2)
m.add_product("Banana", 5, 3)
m.buy_product("Apple", 3)
print(m.total_value())  # 29
