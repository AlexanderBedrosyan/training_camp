# Tracker: списък от потребители, метод most_active_user()

from user import User

class Tracker:
    def __init__(self):
        self.list_of_users: list[User] = []

    def add_user(self, user: User):
        self.list_of_users.append(user)

    def most_active_user(self) -> User | None:
        if not self.list_of_users:
            return None

        most_active = self.list_of_users[0]
        for u in self.list_of_users[1:]:
            if u.total_calories() > most_active.total_calories():
                most_active = u
        return most_active
