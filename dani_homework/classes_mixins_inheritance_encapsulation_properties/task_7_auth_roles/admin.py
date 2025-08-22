# Admin използва миксина, има reset на парола
from user import User
from role import RoleMixin

class Admin(User, RoleMixin):
    def __init__(self, username=str, password=str, ):
        User.__init__(self, username, password)
        RoleMixin.__init__(self)


    def reset_password(self, new_password=str):
        self._User__password = new_password



