# User: списък от активности, метод total_calories()
from activity import Activity

class User:
    def __init__(self, name: str):
        self.name = name
        self.list_of_activity: list[Activity] = []

    def add_activity(self, activity: Activity):
        self.list_of_activity.append(activity)

    def total_calories(self) -> float:
        total = 0.0
        for act in self.list_of_activity:
            total += act.calories
        return total

    def __str__(self):
        return f"{self.name} – {len(self.list_of_activity)} активности, {self.total_calories()} kcal"
