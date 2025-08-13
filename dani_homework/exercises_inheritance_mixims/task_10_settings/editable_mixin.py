#EditableMixin: дава възможност за get, set,
# delete на атрибути чрез getattr, getattr, delattr

class EditableMixin:
    def get_attr(self, name:str):
        return getattr(self, f"_Config__{name}")

    def set_attr(self, name, value):
        setattr(self, f"_Config__{name}", value)

    def del_attr(self, name):
        delattr(self, f"_Config__{name}")