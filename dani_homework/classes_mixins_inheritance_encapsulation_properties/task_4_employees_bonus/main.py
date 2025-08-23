from developer import Developer
from manager import Manager

dev = Developer("Nina", 3000, "senior")
print(dev.code())

mgr = Manager("Max", 5000)
mgr.add_employee(dev)
print(mgr.total_team_salary())  # 8000