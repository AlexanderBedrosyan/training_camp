# LoggerMixin: записва всички действия

class LoggerMixin:
    def __init__(self):
        self._logs = []

    def log(self, logtext=str):
        self._logs.append(logtext)

    def get_logs(self):
        return list(self._logs)