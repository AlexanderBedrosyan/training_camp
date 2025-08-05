# Създай клас TrackedMachine(Machine, UsageTracker)
from machine import Machine
from tracker import UsageTracker

class TrackedMachine(Machine, UsageTracker):
    def __init__(self, hours_used):
        Machine.__init__(self)
        UsageTracker.__init__(self, hours_used)


# Примерен вход:

m1 = TrackedMachine(10)
print(TrackedMachine.machines_created)
m2 = TrackedMachine(25)
print(TrackedMachine.machines_created)  # 2