# Създай клас Tool. След създаване:
# добави нов обикновен атрибут weight чрез setattr()
# използвай getattr() и hasattr() за извличане и проверка
# Примерен вход:
# t = Tool()
# setattr(t, "weight", 3.5)
# if hasattr(t, "weight"):
# print(getattr(t, "weight"))  # 3.5
#-------------------------------------------------------------
class Tool:
    def __init__(self):
        pass  # няма атрибути по подразбиране

t = Tool()

# Добавяне на нов атрибут "weight"
setattr(t, "weight", 3.5)

# Проверка дали атрибутът съществува и извличане на стойността
if hasattr(t, "weight"):
    print(getattr(t, "weight"))  # 3.5


