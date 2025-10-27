from email import Email
from sms import SMS
from push_notification import PushNotification

messages = [Email(), SMS(), PushNotification()]
for m in messages:
    print(m.send("Hello!"))