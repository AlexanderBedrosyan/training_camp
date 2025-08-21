# Създай клас Robot с метод __compute() и атрибут __power_level.
# Достъпи и двете от външен код чрез name mangling.
# ---------------------------------------------------------------

class Robot:
    def __init__(self, power_level: int):
        self.__power_level = power_level    # private атрибут (int)

    def __compute(self) -> str:             # private метод, връща str
        if self.__power_level > 80:
            return "High performance"
        elif self.__power_level > 40:
            return "Normal performance"
        else:
            return "Low performance"


# инстанция за Robot
r = Robot(85)

#  викаме __power_level чрез name mangling
power = r._Robot__power_level  # -> int
print(f"Power level:", power)

# викаме __compute чрез name mangling
status = r._Robot__compute()   # -> str
print(f"Status:", status)
