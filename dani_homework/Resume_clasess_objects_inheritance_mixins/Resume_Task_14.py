# Създай Mixin EncryptMixin с метод encrypt(data), връщащ "Encrypted {data}".
# Създай клас File, който има filename, и клас SecureFile, който наследява File и използва EncryptMixin.
# Добави метод secure_save() в SecureFile, който връща "Saving {encrypted filename}".
# ---------------------------------------------------------------------------------

from Resume_clasess_objects_inheritance_mixins.All_Mixins import EncryptMixin

#
class File:
    def __init__(self, filename):
        self.filename = filename

#
class SecureFile(File, EncryptMixin):
    def secure_save(self):
        encrypted_filename = self.encrypt(self.filename)
        return f"Saving {encrypted_filename}"

# Тест
sf = SecureFile("My_File.txt")
print(sf.secure_save())