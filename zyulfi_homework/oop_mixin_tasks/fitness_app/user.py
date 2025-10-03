# User
# Атрибути: username, private __tracker
# Метод: get_tracker()
from oop_mixin_tasks.fitness_app.tracker import Tracker


class User:
    def __init__(self, username=str):
        self.username = username
        self.__tracker = Tracker()

    def get_tracker(self):
        return self.__tracker
