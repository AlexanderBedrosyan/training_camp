# Атрибути: name, private __customers (списък от Customer)
# Методи:
# add_customer(customer) → добавя клиент
# total_assets() → връща общата сума на всички сметки
# richest_customer() → връща клиента с най-много пари
from customer import Customer


class Bank:
    def __init__(self, name=str):
        self.name = name
        self.__customers: list[Customer] = []

    def add_customer(self, curr_customer) -> None:
        self.__customers.append(curr_customer)

    def total_assets(self) -> int:
        all_balance = 0
        for curr_customer in self.__customers:
            all_balance += curr_customer.total_balance()
        return all_balance

    def richest_customer(self) -> object:
        best_balance = 0
        best_customer = None
        for curr_customer in self.__customers:
            if best_balance <= curr_customer.total_balance():
                best_balance = curr_customer.total_balance()
                best_customer = curr_customer
        return best_customer