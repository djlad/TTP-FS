from .database import db

class Transaction(db.Model):
    __tablename__ = "transactions"
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    transactionPrice = db.Column(db.Float, nullable=False)
    buyerId = db.Column(db.Integer, db.ForeignKey('app_user.id'), nullable=False)