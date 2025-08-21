# LoginMixin с методи login() и logout(),
# поддържа флаг is_logged_in

class LoginMixin:
    def __init__(self):
        self.is_logged_in = False   # поддържа флаг is_logged_in

    def login(self):
        self.is_logged_in = True

    def logout(self):
        self.is_logged_in = False

