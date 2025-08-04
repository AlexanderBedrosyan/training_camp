# Задача 4
# Създай Mixin клас LogMixin с метод log(message), който принтира:
# [LOG]: {message}.

class LogMixin:
    def log(message=str) -> None:
        print(f"[LOG]: {message}")

