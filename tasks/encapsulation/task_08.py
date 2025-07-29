# Създай клас Logger, който има метод log() и използва setattr() за да добавя нови динамични атрибути (напр. log level, timestamp и т.н.).

class Logger:

    def log(self):
        setattr(Logger, 'level', 13)
        setattr(Logger, 'timestamp', 'hours')
        setattr(Logger, 'log', 'Trosho')


logger = Logger()
logger.log()

print(logger.level)
print(logger.timestamp)
print(logger.log)