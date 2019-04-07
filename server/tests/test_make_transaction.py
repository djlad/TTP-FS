import unittest
from app.services import make_transaction


class TestMakeTransaction(unittest.TestCase):
    def test_make_purchase(self):
        make_transaction.make_purchase("aapl", 10)

if __name__ == "__main__":
    unittest.main()