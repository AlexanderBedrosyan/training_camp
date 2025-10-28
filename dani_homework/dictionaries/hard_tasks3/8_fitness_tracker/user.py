# User
# Атрибути: name, private __activities
# Методи: add_activity(activity)
# total_calories()
from activity import Activity


class User:
    def __init__(self, name):
        self.name = name
        self.__activity: list[Activity] = []

    def add_activity(self, activity:Activity):
        self.__activity.append(activity)

    def total_calories(self):
        total_cal = 0
        for curr_activity in self.__activity:
            total_cal += curr_activity.calories
        return  total_cal