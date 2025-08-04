# Public	self.name	Достъпно отвсякъде
# Protected	self._name	По конвенция: "вътрешно" използване
# Private	self.__name	Скриване чрез name mangling

#-------------------------------------------------------------------
# При използване на __име (две долни черти), Python променя името,
# за да не може да се достъпи директно отвън. Това е name mangling.
#
# class SecretBox:
#     def __init__(self):
#         self.__code = "1234"  # private
#
# box = SecretBox()
#
# # print(box.__code)           ❌ Грешка: няма такъв атрибут
# print(box._SecretBox__code)   ✅ Name mangling

#------------------------------------------------------------------
# Name Mangling на метод
# class Safe:
#     def __init__(self):
#         self.__lock_code = "0000"
#
#     def __unlock(self):
#         print("Unlocked!")
#
#
# safe = Safe()
#
# # safe.__unlock()     ❌ AttributeError
# safe._Safe__unlock()  ✅ Работи

#-----------------------------------------------------------------
# Built-in функции за атрибути
# class User:
#     def __init__(self):
#         self.username = "admin"
#
# u = User()
# print(getattr(u, "username"))     # admin
# setattr(u, "username", "guest")   # променя стойността
# print(hasattr(u, "username"))     # True
# delattr(u, "username")
#-----------------------------------------------------------------

# Инстанс атрибути се дефинират чрез self – те са индивидуални за всеки обект.
# Клас атрибути са споделени от всички обекти.
#class Dog:
#     species = "Canine"  # Клас атрибут
#
#     def __init__(self, name):
#         self.name = name  # Инстанс атрибут
#
# d1 = Dog("Rex")
# d2 = Dog("Bella")
#
# print(d1.species)  # Canine
# print(d2.species)  # Canine
#
# Dog.species = "Wolf"
# print(d1.species)  # Wolf (защото species e променен за класа)
#
#


