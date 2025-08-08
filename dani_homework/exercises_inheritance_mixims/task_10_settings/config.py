# Config: клас с private атрибути __theme, __language
from exercises_inheritance_mixims.task_10_settings.editable_mixin import EditableMixin


class Config(EditableMixin):
    def __init__(self, theme:str, language:str):
        self.__theme = theme
        self.__language = language


