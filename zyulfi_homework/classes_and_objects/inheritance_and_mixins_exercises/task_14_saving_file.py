# Задача 14
# Създай Mixin EncryptMixin с метод encrypt(data), връщащ "Encrypted {data}".
# Създай клас File, който има filename, и клас SecureFile, който наследява File и използва EncryptMixin.
# Добави метод secure_save() в SecureFile, който връща "Saving {encrypted filename}".

from mixins.task_14_EncryptMixin import EncryptMixin

class File:
    def __init__(self, filename):
        self.filename = filename

class SecureFile(File, EncryptMixin):
    def secure_save(self):
        return f"Saving {self.encrypt(self.filename)}"

file_name = input("Enter name of file: ")
current_file = SecureFile(file_name)

print(current_file.secure_save())