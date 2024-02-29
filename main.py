from exceptions import RegistrationError, AuthenticationError, MovieNotFoundError, InvalidInputError
from models.movie import Movie
from management.movie_management import MovieManagement
from models.user import User
from management.user_magement import UserManagement


def main():
    """
        Main function to run the Movie Management Application.

        This function provides a command-line interface for users to interact with
        the movie management system. It supports operations such as user login,
        adding and deleting movies (admin only), and adding ratings and reviews to movies.
        The function loops continuously, presenting a menu of options until the user chooses to exit.
    """
    user_management = UserManagement()
    movie_management = MovieManagement(user_management)
    # predefined two admins
    founder = User(user_id=0, username="selina", email="selina06@bu.edu", password="123456", is_admin=True)
    admin = User(user_id=1, username="sarah", email="sarah@example.com", password="123456", is_admin=True)
    # use tuple to store the admin, because tuple is immutable
    admins = (founder, admin)
    for admin in admins:
        user_management.users[admin.email] = admin
        user_management.registered_emails.add(admin.email)

    # add predefined movies
    for name, description, release_date, rate in movies_to_add:
        movie = Movie(id=len(movie_management.movies) + 1, name=name, description=description,
                      release_date=release_date, rate=rate)
        movie_management.add_movie(movie, founder.email)

    while True:
        print("\nWelcome to the Movie Management System")
        print("0. Sign up")
        print("1. Log in")
        print("2. Add movie (Admin only)")
        print("3. Delete movie (Admin only)")
        print("4. Add review (login users only)")
        print("5. Update rating(login users only)")
        print("6. Display all movies")
        print("7. Get movie by id")
        print("8. Exit")
        command = input("Please enter your choice: ").lower()

        # sign up as new user
        if command == "0":
            email = input("Enter email: ")
            username = input("Enter username: ")
            password = input("Enter password: ")

            try:
                user_management.verify_user(email, password, username)
                user_management.add_user(email, username, password)
                print("User registered successfully.")
            except InvalidInputError as e:
                print(e.message)
            except RegistrationError as e:
                print(e.message)

        # log in as exist user
        elif command == "1":
            email = input("Enter email: ")
            password = input("Enter password: ")
            try:
                user_management.login(email, password)
                print("Login successful.")
            except AuthenticationError as e:
                print(e.message)

        # add the new movie
        elif command == "2":
            user_email = input("Please confirm your email: ")
            movie_name = input("Enter movie name: ").strip()
            rate = input("Enter the rate: ").strip()
            description = input("Enter movie description: ").strip()
            release_date = input("Enter movie release year: ").strip()

            try:
                movie_management.verify_movie(movie_name, rate, description, release_date)
                movie = Movie(id=len(movie_management.movies) + 1, name=movie_name, rate=rate, description=description,
                              release_date=release_date)
                movie_management.add_movie(movie, user_email)
                print(f"Movie '{movie.name}' added successfully.")

            except InvalidInputError as e:
                print(e.message)
            except AuthenticationError as e:
                print(e.message)

        # delete the  movie
        elif command == "3":
            user_email = input("Please confirm your email: ")
            movie_id = int(input("Enter movie ID to delete: "))
            try:
                movie = movie_management.delete_movie(movie_id, user_email)
                print(f"Movie: {movie.name} deleted successfully.")
            except AuthenticationError as e:
                print(e.message)
            except MovieNotFoundError as e:
                print(e.message)
            except InvalidInputError as e:
                print(e.message)

        # add review for an exist movie
        elif command == "4":
            user_email = input("Please confirm your email: ")
            movie_id = input("Enter movie ID to add the review: ")

            review = input("Write your review: ")
            try:
                movie_management.add_review(movie_id, review, user_email)
            except AuthenticationError as e:
                print(e.message)
            except InvalidInputError as e:
                print(e.message)
            except MovieNotFoundError as e:
                print(e.message)

        # update the rate for the movie
        elif command == "5":
            user_email = input("Please confirm your email: ")
            movie_id = input("Enter movie ID to update the rate: ")
            rating = input("Enter your rating (0-10): ")
            try:
                movie_management.update_rating(movie_id, rating, user_email)
            except AuthenticationError as e:
                print(e.message)
            except MovieNotFoundError as e:
                print(e.message)
            except InvalidInputError as e:
                print(e.message)

        # display movies according to the rate in descending order
        elif command == "6":
            movies_list = list(movie_management.movies.values())  # Convert to list if stored as a dictionary

            print(f"Currently, there are total {len(movies_list)} movies")
            print()

            sorted_movies = sorted(movies_list, key=lambda movie: float(movie.rate), reverse=True)

            for movie in sorted_movies:
                print(movie)
                print("____" * 20)

        elif command == "7":
            movie_id = input("Please enter movie ID for detail information: ")
            try:
                movie = movie_management.get_movie_by_id(movie_id)
                print("_____" * 20)
                print(movie)
            except InvalidInputError as e:
                print(e.message)
            except MovieNotFoundError as e:
                print(e.message)

        # exit the program
        elif command == "8":
            print("Exiting program. Thank you for using our system.")
            break

        # invalid input
        else:
            print("Invalid input, please choose 0 to 7.")


movies_to_add = [
    ("The Devil Wears Prada",
     "A smart but sensible new graduate lands a job as an assistant to Miranda Priestly, "
     "the demanding editor-in-chief of a high fashion magazine.", 2006, 8.4),
    ("Ron's Gone Wrong",
     "The story of Barney, an awkward middle-schooler and Ron, his new walking, talking, digitally-connected device, "
     "which is supposed to be his 'Best Friend out of the Box.'", 2021, 8.9),
    ("COCO", "Aspiring musician Miguel, confronted with his family's ancestral ban on music, "
             "enters the Land of the Dead to find his great-great-grandfather, a legendary singer.", 2017, 9.5),
    ("Natsume's Book of Friends: The Waking Rock and the Strange Visitor",
     "Natsume encounters a small, mysterious spirit at a local shrine.", 2021, 9.3),
    ("Now You See Me", "An F.B.I. Agent and an Interpol Detective track a team of illusionists "
                       "who pull off bank heists during their performances and reward their audiences with the money.",
     2013, 8.8),
    ("Garfield", "Jon Arbuckle buys a second pet, a dog named Odie."
                 " However, Odie is then abducted, and it is up to Jon's cat, Garfield, to find and rescue the canine.",
     2004, 8.2)]

if __name__ == "__main__":
    main()
