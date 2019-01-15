import unittest
from app.recommend import most_popular
import app


class RecTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.create_app("default")
        self.app_ctx = self.app.app_context()
        self.app_ctx.push()

        print(self.app.config["MONGO_DB"])

    def test_create_popular_movie(self):
        print(most_popular.create_movie_popularity(50))

    def test_d(self):
        a = app.mongo_db.a.find()
        print(a.count())
        for i in a:
            print(i)

    def test_get_popular_movies(self):
        top_n = 10
        self.assertEqual(10, len(most_popular.get_popular_movies(top_n)))
        self.assertTrue(isinstance(most_popular.get_popular_movies(top_n), list))


if __name__ == '__main__':
    unittest.main()
