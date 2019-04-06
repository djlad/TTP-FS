import unittest
from app.services import get_stocks


class TestGetStocks(unittest.TestCase):
    def test_get_stocks(self):
        quote = get_stocks.get_stocks("SNAP")
        self.assertTrue(quote.symbol == "SNAP")
        self.assertTrue(quote.open >= 0) 
        self.assertTrue(quote.latestPrice >= 0) 

    def test_get_stocks_invalid_ticker(self):
        quote = get_stocks.get_stocks("SNAP23oijasdfj")
        self.assertTrue(quote.error == "Unknown symbol")

if __name__ == "__main__":
    unittest.main()