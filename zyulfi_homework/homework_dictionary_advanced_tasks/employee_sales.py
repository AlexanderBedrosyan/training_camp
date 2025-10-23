# Задача 5: Продажби на служители
# sales = {
#     "Nina": {"phones": 5, "laptops": 2},
#     "Max": {"phones": 3, "laptops": 4},
#     "Elena": {"phones": 6, "laptops": 1}
# }
# Изисквания:
# Изчисли общия брой продажби на всеки служител.
# Намери служителя с най-много продажби.
# Изведи сортиран списък по общи продажби.

class Employee:
    def __init__(self, sales):
        self.sales = sales

    def total_sales(self):
        total_sales_dict = {}
        for name, sales in self.sales.items():
            total_sales_dict[name] = sum(sales.values())
        return total_sales_dict

    def best_employee(self):
        best_empl = None
        best_sales = 0
        for name, sales in self.total_sales().items():
            if sales >= best_sales:
                best_sales = sales
                best_empl = name
        return best_empl

    def sorted_sales(self):
        return dict(sorted(self.total_sales().items(), key=lambda item: item[1]))


sales = {
    "Nina": {"phones": 5, "laptops": 2},
    "Max": {"phones": 9, "laptops": 4},
    "Elena": {"phones": 6, "laptops": 5}
}

empl = Employee(sales)
print(empl.total_sales())
print(empl.best_employee())
print(empl.sorted_sales())