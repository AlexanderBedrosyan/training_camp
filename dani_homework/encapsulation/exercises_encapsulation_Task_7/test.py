from device import Device
from mixin_power import PowerStatusMixin

class SmartDevice(Device, PowerStatusMixin):
    pass


d1 = SmartDevice()
d1.power_on()
print(SmartDevice.devices_on)  # 1
print(d1.status())             # Powered ON