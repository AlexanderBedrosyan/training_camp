# 🔹 Задача 10
# Създай клас Device с атрибут status="off". Добави метод toggle() сменящ между "on" и "off".
# Създай клас Smartphone, наследяващ Device, и добави метод call(number) връщащ "Calling {number}".
# Създай клас SmartWatch, наследяващ Device, с метод measure_heart_rate() връщащ "Heart rate measured".

class Device:

    def __init__(self):
        self.status = "off"

    def toggle(self):
        if self.status == "on":
            self.status = "off"
        else:
            self.status = "on"

class Smartphone(Device):

    def call(self, number):
        return f"Calling {number}"

class SmartWatch(Device):

    def measure_heart_rate(self):
        return "Heart rate measured"

smartphone = Smartphone()
print(smartphone.call(859826))
print(smartphone.status)
smartphone.toggle()
print(smartphone.status)

smartwatch = SmartWatch()
print(smartwatch.measure_heart_rate())
print(smartwatch.status)
smartwatch.toggle()
print(smartwatch.status)

