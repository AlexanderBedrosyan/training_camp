# Задача 4
# Създай клас Lamp, който има атрибут is_on (True/False).
# Добави метод switch(), който сменя състоянието на лампата от включено
# към изключено и обратно.

class Lamp:
    def __init__(self, is_on):
        self.is_on = is_on

    def switch (self):
        if self.is_on is True:
            self.is_on = False
        elif self.is_on is False:
            self.is_on = True
        else:
            print("Enter the correct state of the lamp. It can be on/true or off/false.")


current_lapm = Lamp(True)
current_lapm.switch()
print(current_lapm.is_on)
