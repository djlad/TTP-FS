import unittest
from app.services import get_stock


class TestGetStocks(unittest.TestCase):
    def test_get_stocks(self):
        quote = get_stock.get_stock("SNAP")
        self.assertTrue(quote.symbol == "SNAP")
        self.assertTrue(quote.open >= 0) 
        self.assertTrue(quote.latestPrice >= 0) 

    def test_get_stocks_invalid_ticker(self):
        quote = get_stock.get_stock("SNAP23oijasdfj")
        self.assertTrue(quote.error == "Unknown symbol")

if __name__ == "__main__":
    unittest.main()