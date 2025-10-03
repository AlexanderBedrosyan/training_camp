# Route
# Атрибути: start, end, distance

class Route:
    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance

    def __str__(self):
        return f"Distance from {self.start} to {self.end} is {self.distance}"

