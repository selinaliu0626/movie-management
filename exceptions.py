# custom exception classes for my program


class RegistrationError(Exception):
    # Exception raised for errors during the registration process
    def __init__(self, message="Registration error occurred"):
        self.message = message
        super().__init__(self.message)


class AuthenticationError(Exception):
    # Exception raised for errors during the authentication process
    def __init__(self, message="Authentication error occurred"):
        self.message = message
        super().__init__(self.message)


class MovieNotFoundError(Exception):
    # Exception raised when a movie is not found in the database.
    def __init__(self, message="Movie not found"):
        self.message = message
        super().__init__(self.message)


class InvalidInputError(Exception):
    # Exception raised for errors due to invalid input.
    def __init__(self, message="Invalid input provided"):
        self.message = message
        super().__init__(self.message)
