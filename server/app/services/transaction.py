from models.usermodel import UserModel
from models.transaction import Transaction
from models.database import db
from services.get_stock import get_stock

from sqlalchemy.sql import func


def make_purchase(symbol, quantity, buyerId):
    symbol = symbol.upper()
    quote = get_stock(symbol)

    if quote.error:
        return quote.error
    
    new_purchase = Transaction()
    new_purchase.symbol = symbol
    new_purchase.quantity = quantity
    new_purchase.transactionPrice = quote.latestPrice
    new_purchase.buyerId = buyerId
    db.session.add(new_purchase)
    db.session.commit()

    return ""

def sum_transactions(userId):
    ''' Sums up transactions for displaying
        current shares in a portfolio'''
    portfolio = db.session.query(Transaction.symbol, func.sum(Transaction.quantity).label('quantity'))
    portfolio = portfolio.filter(Transaction.buyerId == userId)
    portfolio = portfolio.group_by(Transaction.symbol)
    portfolio = portfolio.having(func.sum(Transaction.quantity) > 0)
    return portfolio