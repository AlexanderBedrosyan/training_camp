# Задача 4
# Създай Mixin клас LogMixin с метод log(message), който принтира:
# [LOG]: {message}.
# Създай клас App с атрибут name, наследяващ LogMixin, и извикай log с името.

from mixins.task_04_LogMixin import LogMixin

class App(LogMixin):
    def __init__(self, name=str):
        self.name = name
        LogMixin.log(name)

current_app = App("Gugov")

