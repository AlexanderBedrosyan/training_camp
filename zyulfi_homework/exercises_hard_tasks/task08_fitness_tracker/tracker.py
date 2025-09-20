# Tracker: списък от потребители, метод most_active_user()
from user import User

class Tracker:
    def __init__(self):
        self.list_of_users: list[User] = []

    def add_user(self, curr_user) -> None:
        self.list_of_users.append(curr_user)

    def most_active_user(self):
        best_user = None
        all_calories = 0
        for curr_user in self.list_of_users:
            if curr_user.total_calories() >= all_calories:
                all_calories = curr_user.total_calories()
                best_user = curr_user
        return best_user
