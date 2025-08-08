from user import User

u = User("admin")
u.login()
print(u.is_logged_in)  # True
u.logout()
print(u.is_logged_in)  # False