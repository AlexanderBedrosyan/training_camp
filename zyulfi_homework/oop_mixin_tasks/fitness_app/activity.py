# Activity
# Атрибути: name, duration, calories_per_min
# Метод: total_calories()

class Activity:
    def __init__(self, name=str, duration=float or int, calories_per_min=float or int):
        self.name = name
        self.duration = duration
        self.calories_per_min = calories_per_min

    def total_calories(self) -> float:
        return self.calories_per_min * self.duration