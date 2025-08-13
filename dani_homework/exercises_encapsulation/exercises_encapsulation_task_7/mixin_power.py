# Mixin PowerStatusMixin с метод status()
# Създай SmartDevice(Device, PowerStatusMixin)

class PowerStatusMixin:
    def status(self):
        return "Powered ON" \
            if self._is_on \
            else "Powered OFF"
