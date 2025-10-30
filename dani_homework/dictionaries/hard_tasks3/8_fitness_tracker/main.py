from activity import Activity
from user import User
from tracker import Tracker

a1 = Activity("Running", 300)
a2 = Activity("Cycling", 500)

u1 = User("Ivan")
u1.add_activity(a1)
u1.add_activity(a2)

t = Tracker()
t.add_user(u1)

print(u1.total_calories())      # 800
print(t.most_active_user())    # Ivan