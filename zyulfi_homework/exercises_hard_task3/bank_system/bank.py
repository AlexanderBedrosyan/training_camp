# Атрибути: private __customers
# Методи:
# add_customer(customer)
# total_assets()
from customer import Customer


class Bank:
    def __init__(self):
        self.__customers: list[Customer] = []

    def add_customer(self, curr_customer=Customer):
        if curr_customer.__class__.__name__ == "Customer":
            self.__customers.append(curr_customer)
        else:
            raise TypeError("Not object")

    def total_assets(self):
        return sum([curr_customer.balance() for curr_customer in self.__customers])
