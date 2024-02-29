class User:
    """
        Represents a user in the Movie Management System.

        This class stores information about a user, including their identification,
        username, email, and administrative status. It also includes methods for
        setting and verifying the user's password.

        Attributes:
            id (int): A unique identifier for the user.
            username (str): The user's username.
            email (str): The user's email address.
            password (str): The user's hashed password. This should not be accessed directly.
            is_admin (bool): A flag indicating whether the user has administrative privileges.
        """

    def __init__(self, user_id, username, email, password, is_admin=False):
        self.id = user_id
        self.username = username
        self.email = email
        self.password = self.__password_hash(password)
        self.is_admin = is_admin

    def __str__(self):
        return f"User(id={self.id}, username={self.username}, email={self.email})"

    def __shift_character(self, char, shift_amount):
        # a help function for create the password_hash
        return chr((ord(char) + shift_amount) % 128)

    def __password_hash(self, password):
        # create a password hash to avoid just use customer's password directly
        res = ""
        for char in password:
            res += char
            res += self.__shift_character(char, 5)
        return res

    def verify_password(self, entered_password):
        # a help function check if customer input password is match our record
        hashed_entered_password = self.__password_hash(entered_password)
        return hashed_entered_password == self.password
