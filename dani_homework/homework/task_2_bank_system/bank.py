# Атрибути: name, private __customers (списък от Customer)
# Методи:
    # add_customer(customer)→ добавя клиент
    # total_assets()        → връща общата сума на всички сметки
    # richest_customer()    → връща клиента с най-много пари
#---------------------------------------------------------------
from customer import Customer


class Bank:
    def __init__(self, name:str):
        self.name = name
        self.__customers: list[Customer] = []

    def add_customer(self, customer):
        self.__customers.append(customer)

    def total_assets(self):
        total_assets = 0
        for curr_customers in self.__customers:
            total_assets += curr_customers.total_balance()

        return total_assets

    def richest_customer(self):
        riches_cut = None
        max_amount = 0

        for curr_cust in self.__customers:
            if max_amount <= curr_cust.total_balance():
                max_amount = curr_cust.total_balance()
                riches_cut = curr_cust

        return riches_cut
