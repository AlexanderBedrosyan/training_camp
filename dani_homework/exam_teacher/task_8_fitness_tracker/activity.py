#Activity: име, продължителност (мин), калории

class Activity:
    def __init__(self, act_name, duration, calories):
        self.act_name = act_name
        self.duration = duration
        self.calories = calories
