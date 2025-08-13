# LoggableMixin: записва всяка операция с време в списък

from datetime import datetime

class LoggableMixin:
    def __init__(self):
        self.logs = []

    def log(self, operation:str):
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        result = f'[{timestamp}] {operation}'
        self.logs.append(result)

