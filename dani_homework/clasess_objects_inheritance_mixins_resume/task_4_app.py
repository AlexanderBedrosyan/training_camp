# Създай Mixin клас LogMixin с метод log(message),
# който принтира: [LOG]: {message}.
# Създай клас App с атрибут name, наследяващ LogMixin,
# и извикай log с името.
# ---------------------------------------------------------------------------

class LogMixin:
    def log(self, message: str)-> None:
        print(f"[LOG]: {message}")

class App(LogMixin):
    def __init__(self, name: str)-> None:
        self.name: str = name

    def start(self)-> None:
        self.log(self.name)

app = App("Mylogs")
app.start()


