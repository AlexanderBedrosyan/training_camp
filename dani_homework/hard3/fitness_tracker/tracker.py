# Tracker
# Атрибути: private __users
# Методи: add_user(user)
# most_active_user()

from user import User

class Tracker:
    def __init__(self):
        self.__users: list[User] = []

    def add_user(self, user: User):
        self.__users.append(user)

    def most_active_user(self) -> User or None:
        if not self.__users:
            return None

        best_u = None
        best_calories = 0
        for u in self.__users:
            total = u.total_calories()
            if total > best_calories:
                best_u = u
                best_calories = total
        return best_u
