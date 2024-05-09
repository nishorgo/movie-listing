from app import MovieListingApp
from movie import Movie


def main():
    app = MovieListingApp()

    # Adding 10 example movies
    app.add_movie(Movie("Inception", "Leonardo DiCaprio, Joseph Gordon-Levitt", "Action", "2010-07-16", "$160 million"))
    app.add_movie(Movie("The Shawshank Redemption", "Tim Robbins, Morgan Freeman", "Drama", "1994-09-23", "$25 million"))
    app.add_movie(Movie("The Godfather", "Marlon Brando, Al Pacino", "Crime", "1972-03-24", "$6-7 million"))
    app.add_movie(Movie("The Dark Knight", "Christian Bale, Heath Ledger", "Action", "2008-07-18", "$185 million"))
    app.add_movie(Movie("Pulp Fiction", "John Travolta, Uma Thurman", "Crime", "1994-10-14", "$8 million"))
    app.add_movie(Movie("Forrest Gump", "Tom Hanks, Robin Wright", "Drama", "1994-07-06", "$55 million"))
    app.add_movie(Movie("The Matrix", "Keanu Reeves, Laurence Fishburne", "Action", "1999-03-31", "$63 million"))
    app.add_movie(Movie("Schindler's List", "Liam Neeson, Ben Kingsley", "Biography", "1993-12-15", "$22 million"))
    app.add_movie(Movie("The Lord of the Rings: The Fellowship of the Ring", "Elijah Wood, Ian McKellen", "Adventure", "2001-12-19", "$93 million"))
    app.add_movie(Movie("Fight Club", "Brad Pitt, Edward Norton", "Drama", "1999-10-15", "$63 million"))

    while True:
        print("\nMovie Listing Application")
        print("1. Register User")
        print("2. Search Movies")
        print("3. Add Movie to Favorites")
        print("4. Remove Movie from Favorites")
        print("5. View User Favorites")
        print("6. Search User Favorites")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            email = input("Enter your email address: ")
            name = input("Enter your name: ")
            age = input("Enter your age: ")
            app.register_user(email, name, int(age))

        elif choice == '2':
            while True:
                search_option = input("Search by:\n1. Title\n2. Cast\n3. Category\nEnter your choice: ")
                if search_option == '1' or search_option == '2' or search_option == '3': break
                else: print("Invalid choice. Please try again.")

            keyword = input("Enter a keyword to search movies: ")
            results = app.search_movies(search_option, keyword)
            print("Movie found: " + str(len(results)))
            print()

            for movie in results:
                print(movie.to_string())
                

        elif choice == '3':
            email = input("Enter your email address: ")
            title = input("Enter movie title to add to favorites: ")
            movie = app.get_movie_details(title)
            if movie:
                app.add_to_favorites(email, movie)
            else:
                print("Movie not found.")

        elif choice == '4':
            email = input("Enter your email address: ")
            title = input("Enter movie title to remove from favorites: ")
            movie = app.get_movie_details(title)
            if movie:
                app.remove_from_favorites(email, movie)
            else:
                print("Movie not found.")

        elif choice == '5':
            email = input("Enter your email address: ")
            user = app.users.get(email)
            if user:
                print(user.to_string())
            else:
                print("User not found.")

        elif choice == '6':
            email = input("Enter your email address: ")
            while True:
                search_option = input("Search by:\n1. Title\n2. Cast\n3. Category\nEnter your choice: ")
                if search_option == '1' or search_option == '2' or search_option == '3': break
                else: print("Invalid choice. Please try again.")

            keyword = input("Enter a keyword to search movies: ")
            results = app.search_movies(search_option, keyword, email)
            print("Movie found: " + str(len(results)))
            print()

            for movie in results:
                print(movie.to_string())

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()