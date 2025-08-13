# 🔹 Задача 12
# Създай клас User с атрибути username и email. Добави метод change_email(new_email),
# който сменя имейла само ако съдържа "@".
# Създай клас Admin, наследяващ User, който добавя метод reset_password() връщащ "Password reset for {username}".
from mixins import MailCheckerMixin

class User(MailCheckerMixin):

    def __init__(self, username=str, email=str):
        self.username = username
        self.email = email

    def change_email(self, new_email) -> None:
        if self.is_valid_mail(new_email):
            self.email = new_email

class Admin(User):

    def reset_password(self) -> str:
        return f"Password reset for {self.username}"

current_admin = Admin("Goshko", "goshakis@abv.bg")
print(current_admin.username)
print(current_admin.email)
new_email = "goshko_gotiniq@abv.bg"
current_admin.change_email(new_email)
print(current_admin.email)
print(current_admin.reset_password())

new_email2 = "goshkotarikata"
current_admin.change_email(new_email2)
print(current_admin.email)