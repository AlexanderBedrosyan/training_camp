from activity import Activity
from user import User

a1 = Activity("Running", 30, 10)
a2 = Activity("Cycling", 40, 8)

u = User("Stefan")
tracker = u.get_tracker()
tracker.add_activity(a1)
tracker.add_activity(a2)

print(tracker.total_burned())  # 30*10 + 40*8 = 620