import unittest
from app.rec import rec
import app


class RecTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.create_app("default")
        self.app_ctx = self.app.app_context()
        self.app_ctx.push()

        print(self.app.config["MONGO_DB"])

    def test_create_popular_movie(self):
        print(rec.create_popular_movies(50))

    def test_get_popular_movies(self):
        top_n = 10
        self.assertEqual(10,len(rec.get_popular_movies(top_n)))
        self.assertTrue(isinstance(rec.get_popular_movies(top_n),list))


if __name__ == '__main__':
    unittest.main()
