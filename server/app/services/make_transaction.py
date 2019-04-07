from models.usermodel import UserModel
from models.transaction import Transaction
from models.database import db
from services.get_stock import get_stock
from services.get_stock import get_stock

def make_purchase(symbol, quantity, buyerId):
    quote = get_stock(symbol)

    if quote.error:
        return False
    
    new_purchase = Transaction()
    new_purchase.symbol = symbol
    new_purchase.quantity = quantity
    new_purchase.transactionPrice = quote.latestPrice
    new_purchase.buyerId = buyerId
    db.session.add(new_purchase)
    db.session.commit()

    return True