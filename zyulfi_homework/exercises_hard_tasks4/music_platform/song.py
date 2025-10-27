# Song
# Атрибути: title, duration
# Метод: __str__()

class Song:
    def __init__(self, title=str, duration=float):
        self.title = title
        self.duration = duration

    def __str__(self):
        return f"The {self.title} is {self.duration} minutes"