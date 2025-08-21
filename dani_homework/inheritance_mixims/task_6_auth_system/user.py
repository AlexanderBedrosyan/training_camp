# User използва миксина,
# има атрибут username

from login_mxin import LoginMixin

class User(LoginMixin):
    def __init__(self, username=str):
        super().__init__()
        self.username = username

