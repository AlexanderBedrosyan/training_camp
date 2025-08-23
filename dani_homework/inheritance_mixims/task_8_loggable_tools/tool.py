# Tool наследява миксина и има метод use()

from inheritance_mixims.task_8_loggable_tools.loggable_mixin import LoggableMixin

class Tool(LoggableMixin):
    def __init__(self, name_of_tool: str):
        super().__init__()
        self.name_of_tool = name_of_tool

    def use(self)-> None:
        self.log(f"{self.name_of_tool} was used")