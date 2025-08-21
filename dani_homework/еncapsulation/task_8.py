# Създай клас Logger, който има метод log() и използва setattr()
# за да добавя нови динамични атрибути (напр. log level, timestamp и т.н.).
# -------------------------------------------------------------------------

from datetime import datetime

class Logger:
    def log(self, level: str, message: str) -> None:
        setattr(self, 'level', level)                    # str
        setattr(self, 'message', message)                # str
        setattr(self, 'timestamp', datetime.now())       # datetime.datetime


# инициализираме логер
logger = Logger()

# викаме метод log()
logger.log("INFO", "System initialized.")

# Достъпваме динамично създадените атрибути
print("Level:", logger.level)        # str
print("Message:", logger.message)    # str
print("Timestamp:", logger.timestamp)  # datetime.datetime
