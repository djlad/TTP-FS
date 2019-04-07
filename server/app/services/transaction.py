from models.usermodel import UserModel
from models.transaction import Transaction
from models.database import db
from services.get_stock import get_stock

from sqlalchemy.sql import func

def buy_stocks(quantity, userId, latestPrice):
    """removes funds if user has enough money to buy shares"""
    if int(quantity) < 0:
        return "Can not buy negative shares."
    user = UserModel.query.get(userId)
    totalcost = float(quantity) * latestPrice
    if user.balance < totalcost:
        return "Insufficient Funds"
    user.balance -= totalcost
    db.session.add(user)
    db.session.commit()
    return ""

def get_num_stocks(symbol, userId):
    '''return number of symbol shares owned by userId'''
    symbol = symbol.upper()
    shares = db.session.query(func.sum(Transaction.quantity)).filter(Transaction.buyerId == userId,
                                                                     Transaction.symbol == symbol)
    if shares:
        return shares.scalar()
    else:
        return 0


def sell_stocks(quantity, userId, latestPrice, symbol):
    """add funds if user has shares to sell.
       quantity must be zero or negative"""
    if float(quantity) > 0:
        return "Quantity of shares to sell must be negative."
    if get_num_stocks(symbol, userId) + quantity < 0:
        return "Insufficient Shares"
    user = UserModel.query.get(userId)
    totalcost = quantity * latestPrice
    user.balance -= totalcost
    db.session.add(user)
    db.session.commit()
    return ""


def make_purchase(symbol, quantity, buyerId):
    '''make purchase or sale of stocks. 
       If quantity is negative this function becomes a sale instead of purchase.
       RETURNS String: contains errors. empty if no errors occur.'''
    print("quantity")
    print(quantity)
    symbol = symbol.upper()
    quote = get_stock(symbol)
    quantity = int(quantity)
    if quote.error:
        return quote.error
    if quantity > 0:
        error = buy_stocks(quantity, buyerId, quote.latestPrice)
    else:
        error = sell_stocks(quantity, buyerId, quote.latestPrice, symbol)
    if error:
        return error
        
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