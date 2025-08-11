# Клас User с:
# protected атрибут _birth_year
# @property age, която изчислява възраст на база текущата година (2025)
from datetime import datetime

class User:
    def __init__(self, birth_year=int):
        self._birth_year = birth_year

    @property
    def age(self):
        current_year = datetime.now().year
        return current_year - self._birth_year