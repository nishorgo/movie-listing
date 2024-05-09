import unittest

from app import MovieListingApp
from movie import Movie

class TestMovieListingApp(unittest.TestCase):
    def setUp(self):
        self.app = MovieListingApp()
        self.app.add_movie(Movie("Inception", "Leonardo DiCaprio, Joseph Gordon-Levitt", "Action", "2010-07-16", "$160 million"))
        self.app.add_movie(Movie("The Shawshank Redemption", "Tim Robbins, Morgan Freeman", "Drama", "1994-09-23", "$25 million"))
        self.app.add_movie(Movie("The Godfather", "Marlon Brando, Al Pacino", "Crime", "1972-03-24", "$6-7 million"))
        self.app.add_movie(Movie("The Dark Knight", "Christian Bale, Heath Ledger", "Action", "2008-07-18", "$185 million"))
        self.app.add_movie(Movie("Pulp Fiction", "John Travolta, Uma Thurman", "Crime", "1994-10-14", "$8 million"))
        
        self.app.register_user("user1@example.com", "user", "20")

    def test_register_user(self):
        self.app.register_user("testuser@example.com", "testuser", "25")
        self.assertIn("testuser@example.com", self.app.users)

    def test_add_movie(self):
        initial_count = len(self.app.movies)
        self.app.add_movie(Movie("Interstellar", "Matthew McConaughey, Anne Hathaway", "Sci-Fi", "2014-11-07", "$165 million"))
        self.assertEqual(len(self.app.movies), initial_count + 1)

    def test_search_movies_by_title(self):
        results = self.app.search_movies('1', 'Inception')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, 'Inception')

    def test_search_movies_by_cast(self):
        results = self.app.search_movies('2', 'Leonardo DiCaprio')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, 'Inception')

    def test_search_movies_by_category(self):
        results = self.app.search_movies('3', 'Drama')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, 'The Shawshank Redemption')

    def test_search_movies_multiple_results(self):
        results = self.app.search_movies('1', 'The')
        self.assertEqual(len(results), 3)
        self.assertEqual(results[0].title, 'The Dark Knight')
        self.assertEqual(results[1].title, 'The Godfather')
        self.assertEqual(results[2].title, 'The Shawshank Redemption')

    def test_add_to_favorites(self):
        email = "user1@example.com"
        movie = self.app.movies[0]
        initial_count = len(self.app.users[email].favorites)
        self.app.add_to_favorites(email, movie)
        self.assertEqual(len(self.app.users[email].favorites), initial_count + 1)

    def test_remove_from_favorites(self):
        email = "user1@example.com"
        movie = self.app.movies[0]
        self.app.add_to_favorites(email, movie)
        initial_count = len(self.app.users[email].favorites)
        self.app.remove_from_favorites(email, movie)
        self.assertEqual(len(self.app.users[email].favorites), initial_count - 1)

    def test_get_user_favorites(self):
        email = "user1@example.com"
        movie = self.app.movies[0]
        self.app.add_to_favorites(email, movie)
        favorites = self.app.get_user_favorites(email)
        self.assertEqual(len(favorites), 1)
        self.assertEqual(favorites[0].title, 'Inception')

    def test_search_user_favorites(self):
        email = "user1@example.com"
        movie = self.app.movies[0]
        self.app.add_to_favorites(email, movie)
        results = self.app.search_movies('1', 'Inception', email)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, 'Inception')

