from email import EmailMessage

e = EmailMessage("Welcome", "user@example.com")
#e = EmailMessage("Welcome", "userexample.com")
e.send()  # Message sent to user@example.com