# Electronics: добавя гаранция в месеци, метод is_under_warranty(months_used)

from product import Product

class Electronics(Product):
    def __init__(self, name=str, price=float, warranty=int) -> None:
        super().__init__(name, price)
        self.warranty = warranty

    def is_under_warranty(self, months_used=int) -> bool:
        under_warranty =  months_used <= self.warranty

        if under_warranty:
            print(f"{self.name} е в гаранция. Остават {self.warranty - months_used} месеца.")
        else:
            print(f"{self.name} не е в гаранция! Изтекла е преди {months_used - self.warranty} месеца.")

        return under_warranty