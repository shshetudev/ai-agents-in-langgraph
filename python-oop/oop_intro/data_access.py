class User:
    def __init__(self, username, email, isAdmin=False):
        self.username = username
        self._email = email  # Private attribute
        self.isAdmin = isAdmin

    def getEmail(self):
        return self._email

    def setEmail(self, new_email):
        if "@" in new_email:
            self._email = new_email

john = User("john", "john@gmail.com", True)
print(john._email) # We should not access private attribute directly, according to the VAN ROUSSUME "consenting adults" principle
print(john.getEmail())

john.setEmail("doe@gmail.com")
print(john.getEmail())


class GoodUser:
    def __init__(self, username, email, isAdmin=False):
        self._email = None
        self.username = username
        self.email = email
        self.isAdmin = isAdmin

    # Getter property
    @property
    def email(self):
        if self.isAdmin:
            return self._email
        print("Not admin, so can't access email")

    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email
        else:
            raise ValueError("Invalid email: no '@'")

doe = GoodUser("doe", "doe@gmail.com", True)
print(doe.email)
doe.email = "doe2@gmail.com"
print(doe.email)
