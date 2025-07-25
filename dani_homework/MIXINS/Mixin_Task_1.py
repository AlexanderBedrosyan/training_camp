# Създай клас LoggerMixin, който има метод log(message),
# който принтира: [LOG]: {message}
# Създай клас User с атрибут name.
# Направи User да наследява и от LoggerMixin.
# Създай обект и извикай log.

class LoggerMixin:
    def log(self, message):
        print(f'[LOG]: {message}')

class User(LoggerMixin):
    def __init__(self, name):
        self.name = name

user1 = User("Ivan")
user1.log(print(f"Потребителят {user1.name} е създаден."))
