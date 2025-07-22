# Задача 3
# Създай клас Phone, който има атрибут brand.
# Добави метод call(), който принтира "{brand} is calling...".

class Phone:
    def __init__(self, brand):
        self.brand = brand

    def call(self):
        print(f"{self.brand} is calling...")

current_phone = Phone("Samsung")
current_phone2 = Phone("Huawei")

Phone.call(current_phone)
Phone.call(current_phone2)