# Създай клас Settings с атрибут theme. Използвай getattr, setattr и hasattr, за да достъпиш, промениш и провериш theme.

class Settings:

    def __init__(self, theme=str):
        self.theme = theme

current_settings = Settings("Black")
print(getattr(current_settings, "theme"))
setattr(current_settings, "theme", "dark")
print(current_settings.theme)
print(getattr(current_settings, "theme"))

print(hasattr(current_settings, "theme"))
print(hasattr(current_settings, "name"))