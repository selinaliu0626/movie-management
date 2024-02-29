from exceptions import RegistrationError, AuthenticationError, InvalidInputError
from models.user import User


class UserManagement:
    """
       Manages user registration, authentication, and roles within the Movie Management System.

       This class handles user accounts, including their creation, authentication, and the management of their roles (e.g., admin status). It interacts with other parts of the system to enforce access control based on user roles.

       Attributes:
           users (dict): A dictionary to store User objects with their email as the key.
           registered_emails(set):A set to store all the users' emails
           login_users (dict): A dictionary tracking the logged-in status of users by their email.
       """
    def __init__(self):
        self.users = {}
        self.registered_emails = set()
        self.login_users = {}
        self.user_id = 2

    def add_user(self, email, username, password):
        # allow user to sign up

        if email in self.registered_emails:
            raise RegistrationError("This user already exists, please log in.")
        new_user = User(user_id=self.user_id, username=username, email=email, password=password)
        self.users[email] = new_user
        self.registered_emails.add(email)
        self.login_users[email] = True
        self.user_id += 1
        return new_user

    def verify_user(self,email, password, username):
        # Check if email contains "@" and is at least 5 characters long
        if "@" in email and len(password) >= 5 and len(username) != 0:
            return True
        else:
            if "@" not in email:
                raise InvalidInputError("Error:Invalid email. Please ensure email must contains '@'.")
            elif len(password) < 5:
                raise InvalidInputError(
                    "Error:Invalid password. Please ensure password must at least have 5 characters")
            else:
                raise InvalidInputError("Error:Invalid username. Please ensure username is not empty")

    def login(self, email, password):
        # allow register user to log in

        if email not in self.registered_emails:
            raise AuthenticationError("User did not match any records, please register as a new user.")
        user = self.users[email]
        if user.verify_password(password):
            self.login_users[email] = True
            return user
        else:
            raise AuthenticationError("Incorrect password, please try again.")

    def logout(self, email):
        # Log the user out
        if email in self.login_users:
            self.login_users[email] = False
            print("Logout successful.")

    def is_logged_in(self, email):
        # Check if the user is logged in
        return self.login_users.get(email, False)
