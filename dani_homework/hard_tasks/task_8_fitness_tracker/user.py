# User: списък от активности, метод total_calories()

class User:
    def __init__(self, name):
        self.name = name
        self.activity_list = []

    def add_activity(self, activity):
        self.activity_list.append(activity)

    def total_calories(self):
        return sum(activity.calories for activity in self.activity_list)