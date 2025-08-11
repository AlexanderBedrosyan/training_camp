# Създай Mixin клас ChargeMixin с метод charge() връщащ "Charging battery...".
# Създай клас Phone, който наследява от ChargeMixin, и извикай метода.
# --------------------------------------------------------------------

from tkinter.font import names

class ChargeMixin:
    def charge(self):
        return "Charging battery..."


class Phone(ChargeMixin):
    def __init__(self, name):
        self.name = name


phone = Phone("iPhone")
print(f"{phone.name}: {phone.charge()}")
