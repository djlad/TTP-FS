import unittest
from services import transaction
from app_factories import create_app_test


class TestMakeTransaction(unittest.TestCase):
    def test_make_purchase(self):
        app = create_app_test('config.DefaultConfig')
        app.app_context().push()
        transaction.make_purchase("aapl", 11, 1)

if __name__ == "__main__":
    unittest.main()