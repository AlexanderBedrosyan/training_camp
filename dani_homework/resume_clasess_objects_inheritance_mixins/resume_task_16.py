# Създай клас Instrument с метод play() връщащ "Playing music".
# Създай клас Guitar, наследяващ Instrument, с метод tune() връщащ "Tuning guitar".
# Създай клас ElectricMixin с метод plug_in() връщащ "Plugged in electric instrument".
# Създай клас ElectricGuitar, който наследява Guitar и използва ElectricMixin,
# добави метод distortion() връщащ "Distortion effect ON".
# -----------------------------------------------------------------------------

from resume_clasess_objects_inheritance_mixins.all_mixins import ElectricMixin


class Instrument:
    def play(self):
        return "Play music"
class Guitar(Instrument):
    def tune(self):
        return "Tuning guitar"
class ElectronicGuitar(Guitar, ElectricMixin):
    def distortion(self):
        return "Distortion effect ON"

elguitar = ElectronicGuitar()

print(elguitar.play())
print(elguitar.tune())
print(elguitar.distortion())
