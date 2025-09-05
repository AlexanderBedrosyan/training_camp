from activity import Activity
from user import User
from tracker import Tracker

u1 = User("Tom")
u2 = User("Sara")

u1.add_activity(Activity("Running", 30, 300))
u1.add_activity(Activity("Cycling", 60, 500))

u2.add_activity(Activity("Walking", 45, 200))
u2.add_activity(Activity("Running", 20, 250))

tracker = Tracker()
tracker.add_user(u1)
tracker.add_user(u2)

print("Most active user:", tracker.most_active_user().name)
