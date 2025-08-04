# Задача 16
# Създай клас Instrument с метод play() връщащ "Playing music".
# Създай клас Guitar, наследяващ Instrument, с метод tune() връщащ "Tuning guitar".
# Създай клас ElectricMixin с метод plug_in() връщащ "Plugged in electric instrument".
# Създай клас ElectricGuitar, който наследява Guitar и използва ElectricMixin,
# добави метод distortion() връщащ "Distortion effect ON".

from mixins.task_16_ElectricMixin import ElectricMixin

class Instrument:
    def play(self) -> str:
        return "Playing music"

class Guitar(Instrument):
    def tune(self):
        return "Tuning guitar"

class ElectricGuitar(Guitar, ElectricMixin):
    def distortion(self):
        return "Distortion effect ON"

current_musical_instrument = ElectricGuitar()

print(current_musical_instrument.play())
print(current_musical_instrument.tune())
print(current_musical_instrument.distortion())
