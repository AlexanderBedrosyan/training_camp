# Tracker
# Атрибути: private __users
# Методи: add_user(user)
# most_active_user()
from user import User


class Tracker:
    def __init__(self):
        self.__users: list[User] = []

    def add_user(self, curr_user):
        self.__users.append(curr_user)

    def most_active_user(self):
        most_ac_u = None
        t_cal = 0

        for curr_u in self.__users:
            if curr_u.total_calories() >= t_cal:
                t_cal = curr_u.total_calories()
                most_ac_u = curr_u.name

        return most_ac_u

