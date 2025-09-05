# Създай клас Device с атрибут status="off".
# Добави метод toggle() сменящ между "on" и "off".
# Създай клас Smartphone, наследяващ Device,
# и добави метод call(number) връщащ "Calling {number}".
# Създай клас SmartWatch, наследяващ Device,
# с метод measure_heart_rate() връщащ "Heart rate measured".
# ----------------------------------------------------------------

class Device:
    def __init__(self, status="off"):
        self.status = "off"

    def toggle(self):
        if self.status == "off":
            self.status = "on"
        else:
            self.status = "off"
        return self.status

class Smartphone(Device):
    def __init__(self, ph_name, status = "off"):
        self.ph_name = ph_name
        super().__init__(status)

    def call(self, number):
        return f"Calling {number}"

class SmartWatch(Device):
    def __init__(self, smwname, status = "off"):
        self.smwname = smwname
        super().__init__(status)

    def measure_heart(self):
        return "Heart rate measured"

sm = Smartphone("iPh", "on")
sm.call(+359885603506)
print(sm.call(+359885603506))

w = SmartWatch("iPh", "off")
w.measure_heart()
print(w.measure_heart())

