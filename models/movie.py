class Movie:
    """
        Represents a movie in the Movie Management System.

        This class stores detailed information about a movie, including its name,
        rating, description, release year, and user reviews. It provides methods to
        manipulate these attributes, such as adding reviews and updating ratings.

        Attributes:
            id (int): A unique identifier for the movie.
            name (str): The name of the movie.
            rate (float): The average rating of the movie, initially set by the creator and updated by user ratings.
            description (str): A brief description of the movie.
            release_date (int): The year the movie was released.
            reviews (list of str): A list of user-submitted reviews for the movie.
        """
    def __init__(self, id, name, rate, description, release_date, rated_people=1, reviews=[]):
        self.id = id
        self.name = name
        self.rate = rate
        self.description = description
        self.release_date = release_date
        self.rated_people = rated_people
        self.reviews = reviews

    def __str__(self):
        # only display the latest review, if the review list is empty, then just show 'Empty'
        review_text = 'Empty' if not self.reviews else ', '.join(self.reviews[-1:])
        return ("Movie: {}\n"
                "Rate: {}\n"
                "Review: {}\n"
                "Description: {}\n"
                "Release Year: {}").format(self.name, self.rate, review_text, self.description, self.release_date)

    def add_review(self, review):
        self.reviews.append(review)

    def set_rating(self, rating):
        self.rate = rating

