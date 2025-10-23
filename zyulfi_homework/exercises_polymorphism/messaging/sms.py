# SMS: връща "Sending SMS: {msg}"
from exercises_polymorphism.messaging.message import Message


class SMS(Message):
    def send(self, msg):
        return f"Sending SMS: {msg}"
    