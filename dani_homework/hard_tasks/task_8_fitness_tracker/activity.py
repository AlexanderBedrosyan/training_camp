#Activity: име, продължителност (мин), калории

class Activity:
    def __init__(self, name: str, duration: int, calories: int)-> None:
        self.name = name
        self.duration = duration
        self.calories = calories

    def __str__(self):
        return f"{self.name} ({self.duration} мин, {self.calories} kcal)"
