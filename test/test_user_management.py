import unittest

from exceptions import RegistrationError
from management.user_magement import UserManagement


class TestUserManagement(unittest.TestCase):
    def setUp(self):
        # Initialize a new UserManagement object before each test.
        self.user_management = UserManagement()

    def test_add_user_success(self):
        # Test adding a new user successfully.
        email = "test@example.com"
        username = "testuser"
        password = "password123"
        result = self.user_management.add_user(email, username, password)
        self.assertIsNotNone(result)
        self.assertEqual(result.email, email)
        self.assertTrue(email in self.user_management.registered_emails)

    def test_add_user_duplicate_email(self):
        # Test adding a user with a duplicate email.
        email = "test@example.com"
        username = "testuser"
        password = "password123"
        self.user_management.add_user(email, username, password)
        # Try to add another user with the same email
        with self.assertRaises(RegistrationError):
            self.user_management.add_user(email, "anotheruser", "anotherpassword")


if __name__ == "__main__":
    unittest.main()
