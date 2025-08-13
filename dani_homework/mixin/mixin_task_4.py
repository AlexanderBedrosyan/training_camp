# Създай TalkMixin с метод talk()
# връщащ "Talking...".
# Направи клас Robot, който наследява от него, и тествай.
# -------------------------------------------------------

class TalkMixin:
    def talk(self):
        print(f"Talking...")

class Robot(TalkMixin):
    pass

robot1 = Robot()
robot1.talk()