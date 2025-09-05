# Създай клас Product със следните елементи:
# private атрибут __price
# обикновен атрибут name
# метод set_discount(percentage) – намалява цената с определен процент
# метод get_price() – връща текущата цена, минимална цена е 0
# Примерен вход:
# p = Product("Shoes", 120)
# p.set_discount(20)
# print(p.get_price())  # 96.0
# ------------------------------------------------------------------

class Product:
    def __init__(self, name = str, price = float)-> None:
        self.name = name
        self.__price = max(price, 0)  # гарантираме, че не е под 0

    def set_discount(self, percentage = float) -> None:
        """Намалява цената с дадения процент. Минималната цена е 0."""
        discount = self.__price * (percentage / 100)
        self.__price = max(self.__price - discount, 0)

    def get_price(self) -> float:
        """Връща текущата цена."""
        return self.__price

# Употреба
p = Product("Shoes", 120)
p.set_discount(20)
print(p.get_price())  # 96.0
