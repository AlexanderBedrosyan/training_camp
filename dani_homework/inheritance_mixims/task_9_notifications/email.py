# EmailMessage: наследява Message, добавя адрес,
# метод send(), който валидира адрес

from inheritance_mixims.task_9_notifications.message import Message
import re

class EmailMessage(Message):
    def __init__(self, content, address):
        super().__init__(content)
        self.address = address

    def validate_address(self):
        # Просто валидиране на email
        return re.match(r"[^@]+@[^@]+\.[^@]+", self.address)

    def send(self):
        if not self.validate_address():
            raise ValueError(f"Invalid email address: {self.address}")
        print(f"Message sent to {self.address}")