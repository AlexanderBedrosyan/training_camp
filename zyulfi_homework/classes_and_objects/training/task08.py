# Задача 8
# Създай клас Logger, който има метод log() и използва setattr() за да добавя нови динамични атрибути
# (напр. log level, timestamp и т.н.).

class Logger:
    def log(self) -> None:
        setattr(Logger, "level", 13)
        setattr(Logger, "timestamp", "minutes")
        setattr(Logger, "log", "trosho")

current_logger = Logger()

current_logger.log()
print(current_logger.level)
print(current_logger.timestamp)
print(current_logger.log)

