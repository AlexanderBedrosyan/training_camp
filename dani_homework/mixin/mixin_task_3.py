# Създай Mixin клас SwimMixin
# с метод swim() връщащ "Swimming...".
# Създай клас Duck, който наследява и от SwimMixin,
# и от FlyMixin (от предходната задача),
# и извикай и двата метода.
# -------------------------------------------------

from mixin.mixin_task_2 import FlyMixin

class SwimMixin:
    def swim(self):
        print(f"Swimming...")

class Duck(SwimMixin, FlyMixin):
    pass

duck = Duck()
duck.swim()
