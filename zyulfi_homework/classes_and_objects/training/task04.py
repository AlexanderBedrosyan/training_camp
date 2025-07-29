# Задача 4
# Създай клас Settings с атрибут theme. Използвай getattr, setattr и hasattr,
# за да достъпиш, промениш и провериш theme.

class Settings:
    def __init__(self, theme=str):
        self.theme = theme

current_settings = Settings("Black")
#
# getattr(obj, name)	Връща стойност на атрибут
# setattr(obj, name, value)	Присвоява стойност
# hasattr(obj, name)	Проверява дали съществува
# delattr(obj, name)

print(getattr(current_settings, "theme"))
setattr(current_settings, "theme", "white")
print(current_settings.theme)
print(hasattr(current_settings, "theme"))
print(hasattr(current_settings, "name"))
