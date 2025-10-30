# Song
# Атрибути: title, duration
# Метод: __str__()
class Song:
    def __init__(self, title: str, duration: float):
        self.title = title
        self.duration = duration  # в минути или секунди (по избор)

    def __str__(self):
        return f"Song('{self.title}', duration={self.duration} min)"
