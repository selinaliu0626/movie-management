import unittest

from exceptions import MovieNotFoundError, AuthenticationError
from models.movie import Movie
from management.movie_management import MovieManagement
from models.user import User
from management.user_magement import UserManagement


class TestMovieManagement(unittest.TestCase):
    def setUp(self):
        # Initialize MovieManagement and UserManagement for each test.
        self.user_management = UserManagement()
        self.movie_management = MovieManagement(self.user_management)
        # Assume admin_user is already added to UserManagement in its __init__ or elsewhere
        self.admin_email = "admin@example.com"
        self.regular_email = "user@example.com"
        # Add test movies
        self.movie_management.movies = {
            1: Movie(id=1, name="Test Movie", description="A test movie", release_date=2020, rate=8.5)
        }
        # Add a test admin user and a regular user
        self.user_management.users = {
            self.admin_email: User(user_id=-1, email=self.admin_email, username="admin", password="adminpass",
                                   is_admin=True),
            self.regular_email: User(user_id=-2, email=self.regular_email, username="user", password="userpass",
                                     is_admin=False)
        }
        self.user_management.logged_in_status = {self.admin_email: True, self.regular_email: False}

    def test_add_movie_by_admin(self):
        # Test that an admin can successfully add a movie.
        new_movie = Movie(id=2, name="New Movie", description="Another test movie", release_date=2021, rate=9)
        self.movie_management.add_movie(new_movie, self.admin_email)
        self.assertIn(2, self.movie_management.movies)

    def test_delete_movie_by_admin(self):
        # Test that an admin can successfully delete a movie.
        self.movie_management.delete_movie(1, self.admin_email)
        self.assertNotIn(1, self.movie_management.movies)

    def test_add_review_by_unauthenticated_user_raises_error(self):
        # Test adding a review by an unauthenticated user raises an AuthenticationError.
        with self.assertRaises(AuthenticationError):
            self.movie_management.add_review(1, "Great movie!", self.regular_email)


if __name__ == '__main__':
    unittest.main()
