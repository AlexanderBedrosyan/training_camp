# Task_16
# Създай клас Instrument с метод play() връщащ "Playing music".
# Създай клас Guitar, наследяващ Instrument, с метод tune() връщащ "Tuning guitar".
# Създай клас ElectricMixin с метод plug_in() връщащ "Plugged in electric instrument".
# Създай клас ElectricGuitar, който наследява Guitar и използва ElectricMixin,
# добави метод distortion() връщащ "Distortion effect ON".

class ElectricMixin:
    def plug_in(self):
        return "Plugged in electric instrument"
#-----------------------------------------------------------------------------------

# Task_14
# Създай Mixin EncryptMixin с метод encrypt(data), връщащ "Encrypted {data}".
# Създай клас File, който има filename, и клас SecureFile, който наследява File и използва EncryptMixin.
# Добави метод secure_save() в SecureFile, който връща "Saving {encrypted filename}".

class EncryptMixin:
    def encrypt(self, data):
        return f"Encrypted {data}"

#--------------------------------------------------------------------------------------