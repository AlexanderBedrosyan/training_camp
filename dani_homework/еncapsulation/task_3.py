# Създай клас Car с protected атрибут _engine.
# Добави метод start() и принтирай "Engine started".
# ---------------------------------------------------

class Car:
    def __init__(self, engine):
        self._engine = engine       # защитен атрибут

    def start(self):
        print("Engine started")     # отпечатва, без да връща стойност None by def

# Създаваме обект с конкретен двигател
mycar = Car("Tesla")
result = mycar.start()                      # Принтира "Engine started"

