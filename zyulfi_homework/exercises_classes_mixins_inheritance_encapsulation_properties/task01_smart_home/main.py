from light import Light
from thermostat import Thermostat

l = Light()
# l.turn_on()
print(l._status)
l.brightness = 80
print(l.brightness)
print(l._status)# 80

t = Thermostat()
t.temperature = 25
print(t.temperature)  # 25

# l.brightness = 120
# t.temperature = 45

