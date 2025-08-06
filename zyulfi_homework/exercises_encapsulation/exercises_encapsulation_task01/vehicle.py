# Клас Vehicle със:
# protected атрибут _type
# метод start(), който отпечатва "Starting {type}"

class Vehicle:
    def __init__(self, current_type):
        self._type = current_type

    def start(self):
        print(f"Starting {self._type}")