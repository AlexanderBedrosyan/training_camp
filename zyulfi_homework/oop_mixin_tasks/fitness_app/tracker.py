# Tracker (CalorieMixin)
# Атрибути: private __activities
# Методи: add_activity(), total_burned()
from oop_mixin_tasks.fitness_app.activity import Activity
from oop_mixin_tasks.fitness_app.calorie_mixin import CalorieMixin


class Tracker(CalorieMixin):
    def __init__(self):
        self.__activities: list[Activity] = []

    def add_activity(self, curr_activity) -> None:
        self.__activities.append(curr_activity)

    def total_burned(self) -> float:
        return sum([curr_activity.total_calories() for curr_activity in self.__activities])