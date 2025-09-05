# Създай клас User с атрибути username и email.
# Добави метод change_email(new_email), който сменя имейла само ако съдържа "@".
# Създай клас Admin, наследяващ User,
# който добавя метод reset_password() връщащ "Password reset for {username}".
#--------------------------------------------------------------------------

class User:
    def __init__(self, username: str, email: str)-> None:
        self.username = username
        self.email = email

    def change_email(self, new_email: str)-> str:
        if "@" in new_email:
            self.email = new_email
            return f"Email changed to {new_email}"
        return "Invalid email address, missing @"

class Admin(User):
    def __init__(self, username: str, email: str)->None:
        super().__init__(username, email)

    def reset_password(self)-> str:
        return f"Password reset for {self.username}"

# Тест
user = User("MyName", "MyName@myself.bg")
print(user.change_email("MyNamemyself.bg"))       # Error
print(user.change_email("mynameis@myself.bg"))    # Email changed to mynameis@myself.bg

admin = Admin("admin_user", "admin@myself.bg")
print(admin.reset_password())                     # Password reset for admin_user