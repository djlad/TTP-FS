import unittest
from services import transaction
from app_factories import create_app_test


class TestTransaction(unittest.TestCase):
    def test_make_purchase(self):
        app = create_app_test('config.DefaultConfig')
        app.app_context().push()
        transaction.make_purchase("aapl", 11, 7)
    
    def test_get_num_stocks(self):
        app = create_app_test('config.DefaultConfig')
        app.app_context().push()
        ns = transaction.get_num_stocks('AAPL', 7)
        print(ns)
        self.assertTrue(ns > 0)


if __name__ == "__main__":
    unittest.main()