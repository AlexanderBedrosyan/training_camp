from developer import Developer
from manager import Manager
from intern import Intern

employees = [Developer(2000, 500), Manager(3000, 1000), Intern(800)]
for e in employees:
    print(e.calculate_salary())