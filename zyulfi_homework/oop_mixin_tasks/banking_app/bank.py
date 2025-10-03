# Bank
# Атрибути: private __customers
# Методи: add_customer(), find_customer(name)
from oop_mixin_tasks.banking_app.customer import Customer


class Bank:
    def __init__(self):
        self.__customers: list[Customer] = []

    def add_customer(self, curr_customer) -> None:
        self.__customers.append(curr_customer)

    def find_customer(self, name):
        for curr_customer in self.__customers:
            if curr_customer.name == name:
                return curr_customer
        return None