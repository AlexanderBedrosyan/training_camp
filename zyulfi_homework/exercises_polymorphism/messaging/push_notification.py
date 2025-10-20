# PushNotification: връща "Sending push notification: {msg}"
from exercises_polymorphism.messaging.message import Message


class PushNotification(Message):
    def send(self, msg):
        return f"Sending push notification: {msg}"