from light import Light
from thermostat import Thermostat

l = Light()
l.turn_on()
l.brightness = 80
print(l.brightness)  # 80

t = Thermostat()
t.temperature = 25
print(t.temperature)  # 25