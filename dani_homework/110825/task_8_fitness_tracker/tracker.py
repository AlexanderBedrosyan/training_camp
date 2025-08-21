# Tracker: списък от потребители, метод most_active_user()
from user import User


class Tracker:
    def __init__(self):
        self.list_of_users = []

    def add_user(self, user):
        self.list_of_users.append(user)

    def most_active_user(self):
        if not self.list_of_users:
            return None

        most_active_user = self.list_of_users[0]
        for user in self.list_of_users[1:]:
            if user.total_calories() > most_active_user.total_calories():
                most_active_user = user
        return most_active_user