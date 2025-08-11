from manager import Manager
from employee import Employee

m = Manager("Laura", 3000)
m.add_employee(Employee("Ivan", 2000))
m.add_employee(Employee("Mira", 2200))
print(m.total_salary())  # 7200