# Email: връща "Sending email: {msg}"
from exercises_polymorphism.messaging.message import Message


class Email(Message):
    def send(self, msg):
        return f"Sending email: {msg}"
    