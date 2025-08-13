# Създай клас Car с protected атрибут _engine. Добави метод start() и принтирай "Engine started".

class Car:

    def __init__(self, engine=str):
        self._engine = engine

    def start(self) -> None:
        print(f"{self._engine} started")


current_car = Car("Trabant")
current_car.start()