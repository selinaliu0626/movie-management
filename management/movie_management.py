from exceptions import AuthenticationError, MovieNotFoundError, InvalidInputError


class MovieManagement:
    """
        Manages the collection of movies in the Movie Management System.

        This class provides functionalities to add, delete, and update movies within the system. It also allows for adding reviews and ratings to movies. Administrative actions such as adding and deleting movies are restricted to users with admin privileges.

        Attributes:
            movies (dict): A dictionary to store movies with their ID as the key.
            user_management (UserManagement): An instance of UserManagement to check user permissions and login status.
        """

    def __init__(self, user_management):
        self.movies = {}
        self.user_management = user_management

    def add_movie(self, movie, email):
        # only admins could add movies
        user = self.user_management.users[email]
        if not user or not user.is_admin:
            raise AuthenticationError("Error: Only admins can add movies.")
        self.movies[movie.id] = movie
        return movie

    def delete_movie(self, movie_id, email):
        # Only admins could delete movies
        user = self.user_management.users.get(email)
        if not user or not user.is_admin:
            raise AuthenticationError("Error: Only admins can delete movies.")
        if movie_id in self.movies:
            movie_to_delete = self.movies[movie_id]
            del self.movies[movie_id]
            return movie_to_delete
        else:
            raise MovieNotFoundError(f"Error: Movie with ID {movie_id} not found.")

    def verify_movie_id(self, movie_id):
        if not movie_id.isdigit():
            raise InvalidInputError("Error: movie id must be an integer")
        elif int(movie_id) not in self.movies:
            raise MovieNotFoundError(f"Error: Movie with ID {movie_id} not found.")
        return True

    def get_movie_by_id(self, movie_id):
        if self.verify_movie_id(movie_id):
            return self.movies[int(movie_id)]

    def add_review(self, movie_id, review, user_email):
        if not self.user_management.is_logged_in(user_email):
            raise AuthenticationError("Error: User must be logged in to add a review.")
        if review == "":
            raise InvalidInputError("Error: The input review can not be empty.")
        if self.verify_movie_id(movie_id):
            movie_id = int(movie_id)
            movie = self.movies[movie_id]
            movie.add_review(review)
            print(f"You have been successfully add a new review to {movie.name}")

    def update_rating(self, movie_id, rating, user_email):
        if not self.user_management.is_logged_in(user_email):
            raise AuthenticationError("Error: User must be logged in to update a rating.")
        if self.is_float(rating):
            if not (0 <= float(rating) <= 10):
                raise InvalidInputError("Error: Rating must range from 0 to 10.")
            else:
                if self.verify_movie_id(movie_id):
                    # Validate the rating value
                    movie_id = int(movie_id)
                    movie = self.movies[movie_id]
                    # calculate the new average rate
                    total_rates = float(movie.rate) * float(movie.rated_people) + float(rating)
                    movie.rated_people += 1
                    new_rate = round(total_rates / movie.rated_people, 2)
                    movie.set_rating(new_rate)
                    print(f"Rating updated for {movie.name}.")
        else:
            raise InvalidInputError("Error: Rating must be an number range from 0 to 10")

    def is_float(self, rate):
        # check is rate could be converted to a float
        try:
            float(rate)
            return True
        except ValueError:
            return False

    def verify_movie(self, movie_name, rate, description, release_date):
        # verify the input for add movie
        if self.is_float(rate) and 0 <= float(rate) <= 10 and len(movie_name) > 0 and len(
                description) > 0 and release_date.isdigit() and 1900 <= int(release_date) <= 2024:
            return True
        else:
            if self.is_float(rate) != True or float(rate) < 0 or float(rate) > 10:
                raise InvalidInputError("Error: rate must be a float range from 0 to 10")
            elif len(movie_name) == 0:
                raise InvalidInputError("Error: movie name could not be empty")
            elif len(description) == 0:
                raise InvalidInputError("Error: description can not be empty")
            else:
                raise InvalidInputError("Error: release date must be an integer range from 1900 to 2024")
