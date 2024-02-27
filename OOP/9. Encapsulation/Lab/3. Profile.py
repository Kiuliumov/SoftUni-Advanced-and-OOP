class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self._validator()

    def _validator(self):
        flag_digit = False
        flag_alpha = False
        for char in self.password:
            if char.isdigit():
                flag_digit = True
            if char.isupper():
                flag_alpha = True
        if not (5 <= len(self.username) <= 15):
            raise ValueError('The username must be between 5 and 15 characters.')
        if not (8 <= len(self.password) and flag_digit and flag_alpha):
            raise ValueError('The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')
    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'
