# Създай клас Settings с атрибут theme.
# Използвай getattr, setattr и hasattr, за да достъпиш, промениш и провериш theme.
# ---------------------------------------------------------------------------

class Settings:
    def __init__(self):
        self.theme = "light"  # Начален theme

# обект
app_settings = Settings()

# 1. hasattr(obj, "theme") за проверка атрибутът 'theme' съществува ли
check = hasattr(app_settings, 'theme')
print("hasattr(app_settings, 'theme') връща:", check)           # -> True

# 2. getattr(obj, "theme") текущата стойност на атрибута 'theme'
current_theme = getattr(app_settings, 'theme')
print("getattr(app_settings, 'theme') връща:", current_theme)   # -> "light"

# 3. setattr(obj, "theme", "dark") променяме стойността на атрибута 'theme' → връща None по подразбиране
result = setattr(app_settings, 'theme', 'dark')
print("setattr(app_settings, 'theme', 'dark') връща:", result)  # -> None

# След промяната
print("Новата стойност на theme е:", app_settings.theme)        # -> "dark"
