# Task_16
# Създай клас Instrument с метод play() връщащ "Playing music".
# Създай клас Guitar, наследяващ Instrument, с метод tune() връщащ "Tuning guitar".
# Създай клас ElectricMixin с метод plug_in() връщащ "Plugged in electric instrument".
# Създай клас ElectricGuitar, който наследява Guitar и използва ElectricMixin,
# добави метод distortion() връщащ "Distortion effect ON".

class ElectricMixin:
    def plug_in(self):
        return "Plugged in electric instrument"

