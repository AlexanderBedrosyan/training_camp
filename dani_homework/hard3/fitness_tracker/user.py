# User
# Атрибути: name, private __activities
# Методи: add_activity(activity)
# total_calories()
from activity import Activity


class User:
    def __init__(self, name:str):
        self.name = name
        self.__activities: list[Activity] = []


    def add_activity(self, activity:Activity):
        self.__activities.append(activity)

    def total_calories(self) -> float:
        return sum(a.get_calories() for a in self.__activities)