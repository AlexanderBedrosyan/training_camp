# Activity: име, продължителност (мин), калории

class Activity:
    def __init__(self, name=str, duration=float, calories=float):
        self.name = name
        self.duration = duration
        self.calories = calories
