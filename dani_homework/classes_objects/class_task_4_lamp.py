# Създай клас Lamp, който има атрибут is_on (True/False).
# Добави метод switch(),
# който сменя състоянието на лампата от включено към изключено и обратно.

class Lamp:
    def __init__(self, is_on=False):
        self.is_on = is_on

    def switch(self):
        self.is_on = not self.is_on
        print(f"Lamp state is on: {self.is_on}")

    def status(self):
        if self.is_on:
            print("Lamp is ON")
        else:
            print("Lamp is OFF")

# Objects
lamp_state_1 = Lamp(True)
lamp_state_2 = Lamp(False)

# Call methods
lamp_state_1.status()   # Lamp is ON
lamp_state_1.switch()   # Lamp state is on: False
lamp_state_1.status()   # Lamp is OFF
print()
lamp_state_2.status()   # Lamp is OFF
lamp_state_2.switch()   # Lamp state is on: True
lamp_state_2.status()   # Lamp is ON