from user import User


class MovieListingApp:
    def __init__(self):
        self.movies = []
        self.users = {}

    def register_user(self, email, name, age):
        if email in self.users:
            print("User already registered.")
        else:
            self.users[email] = User(email, name, age)
            print("User registered successfully.")

    def add_movie(self, movie):
        self.movies.append(movie)

    def search_movies(self, search_option, keyword, email=None):
        results = []

        if email: search_list = self.get_user_favorites(email)
        else: search_list = self.movies

        for movie in search_list:
            if search_option == '1' and keyword.lower() in movie.title.lower():
                results.append(movie)
            elif search_option == '2' and keyword.lower() in movie.cast.lower():
                results.append(movie)
            elif search_option == '3' and keyword.lower() in movie.category.lower():
                results.append(movie)
        results.sort(key=lambda x: x.title)
        return results

    def get_movie_details(self, title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                return movie
        return None

    def add_to_favorites(self, email, movie):
        if email in self.users:
            self.users[email].favorites.append(movie)
            print("Movie added to favorites.")
        else:
            print("User not found.")

    def remove_from_favorites(self, email, movie):
        if email in self.users:
            if movie in self.users[email].favorites:
                self.users[email].favorites.remove(movie)
                print("Movie removed from favorites.")
            else:
                print("Movie not found in favorites.")
        else:
            print("User not found.")

    def get_user_favorites(self, email):
        if email in self.users:
            return self.users[email].favorites
        else:
            print("User not found.")
            return []