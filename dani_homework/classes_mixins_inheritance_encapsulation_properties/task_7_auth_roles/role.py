# RoleMixin: методи add_role() и has_role()

class RoleMixin:
    def __init__(self):
        self._role = set()

    def add_role(self, role=str)->None:
        self._role.add(role)

    def has_role(self, role=str)->bool:
        return role in self._role