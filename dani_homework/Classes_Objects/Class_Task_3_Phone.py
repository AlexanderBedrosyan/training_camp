# Създай клас Phone, който има атрибут brand.
# Добави метод call(), който принтира "{brand} is calling...".

class Phone:
    def __init__(self, brand):
        self.brand = brand  # атрибут brand

    def call(self):
        print(f"{self.brand} is calling...")

# Създаване на обекти
phone_1 = Phone("iPhone")
phone_2 = Phone("Samsung")
phone_3 = Phone("Xiaomi")

phone_1.call()  #
phone_2.call()  #
phone_3.call()  #