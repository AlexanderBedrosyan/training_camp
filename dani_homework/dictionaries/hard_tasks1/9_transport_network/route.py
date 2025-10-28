# Route: начална и крайна точка, разстояние
class Route:
    def __init__(self, start: str, end: str, distance: int):
        self.start = start
        self.end = end
        self.distance = distance

    def __str__(self):
        print(f"Начална точка: {self.start}, Крайна точка: {self.end}, Разстояние: {self.distance} km.")

r = Route("A", "B", 50)
r.__str__()