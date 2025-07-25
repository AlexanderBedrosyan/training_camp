# Задача 4
# Създай клас Lamp, който има атрибут is_on (True/False).
# Добави метод switch(), който сменя състоянието на лампата от включено
# към изключено и обратно.

class Lamp:
    def __init__(self, is_on):
        self.is_on = is_on

    def switch (self):
        if self.is_on == "true":
            print("on")
        elif self.is_on == "false":
            print("off")
        else:
            print("Enter the correct state of the lamp. It can be on/true or off/false.")


current_lapm = Lamp(input("Enter true for on or false for off for the lamp status: "))
Lamp.switch(current_lapm)
