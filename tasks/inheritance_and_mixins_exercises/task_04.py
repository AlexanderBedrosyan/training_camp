# 🔹 Задача 4
# Създай Mixin клас LogMixin с метод log(message), който принтира:
# [LOG]: {message}.
# Създай клас App с атрибут name, наследяващ LogMixin, и извикай log с името.
from mixins import LogMixin


class App(LogMixin):

    def __init__(self, name):
        self.name = name

current_app = App("Gosho")
current_app.log(current_app.name)