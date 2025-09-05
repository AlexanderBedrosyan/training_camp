# Activity
# Атрибути: name, calories

class Activity:
    def __init__(self, name:str, calories: int or float):
        self.name = name
        self.calories = calories

    def get_calories(self):
        return self.calories
