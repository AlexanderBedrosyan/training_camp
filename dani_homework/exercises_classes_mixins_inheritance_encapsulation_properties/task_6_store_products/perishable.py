# Perishable: добавя expiration_date, метод is_expired(today)

from product import Product
from datetime import datetime, date

class Perishable(Product):
    def __init__(self, name=str, price=float, expiration_date=str) -> None:
        super().__init__(name, price)
        self.expiration_date = expiration_date

    def is_expired(self) -> bool:
        expiration_date = datetime.strptime(self.expiration_date, "%d-%m-%Y").date()
        today_date = date.today()

        expired = today_date > expiration_date
        if expired:
            print(f"{self.name} не е в срок! Изтекъл на {expiration_date}")
        else:
            print(f"{self.name} е в срок. Годен до {expiration_date}")

        return expired