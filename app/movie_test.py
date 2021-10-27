import unittest
from models import movie
Movie = movie.Movie

class MovieTest(unittest.TestCase):
    """
    Test class to test the behaviour of the movie class
    """
    def setUp(self):
        """
        Set up method that will run before each test
        """
        self.new_movie = Movie(1234, "Python Must Be Crazy", "A thrilling new python series", "https://image.tmdb.org/t/p/w500/khsjha27hbs", 8.5, 129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie, Movie))


if __name__ == "__main__":
    unittest.main()