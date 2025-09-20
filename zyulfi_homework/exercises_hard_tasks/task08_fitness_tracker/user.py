# User: списък от активности, метод total_calories()
from activity import Activity

class User:
    def __init__(self, name):
        self.name = name
        self.list_of_activity: list[Activity] = []

    def add_activity(self, curr_activity) -> None:
        self.list_of_activity.append(curr_activity)

    def total_calories(self) -> float:
        return sum([curr_activity.calories for curr_activity in self.list_of_activity])
