from admin import Admin

a = Admin("admin", "1234")
a.add_role("superuser")
print(a.has_role("superuser"))  # True

