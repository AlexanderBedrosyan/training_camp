# Perishable: добавя expiration_date, метод is_expired(today)

from product import Product
import datetime


class Perishable(Product):
    today = datetime.datetime.now()

    def __init__(self, name, price, expiration_date):
        super().__init__(name, price)
        self.expiration_date = "2025-08-01"

    def is_expired(self):
        if

