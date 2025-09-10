# Bank
# Атрибути: private __customers
# Методи:
# add_customer(customer)
# total_assets()
from customer import Customer


class Bank:
    def __init__(self):
        self.__customers: list[Customer] = []

    def add_customer(self, current_customer):
        self.__customers.append(current_customer)

    def total_assets(self):
        total_assets = 0
        for current_customer in self.__customers:
            total_assets += current_customer.balance()

        return total_assets

