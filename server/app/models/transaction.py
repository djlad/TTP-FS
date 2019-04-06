from .database import db

class Transaction(db.Model):
    __tablename__ = "transactions"
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(10), nullable=False)
    transactionPrice = db.Column(db.Float, nullable=False)
    buyerId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)