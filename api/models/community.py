from datetime import datetime
from api.models.db import db

class Community(db.Model):
    __tablename__ = 'communities'
    id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(db.Integer, db.ForeignKey('transactions.id'), nullable=False)
    name = db.Column(db.String(100))

    def __init__(self, transaction_id, name):
        self.transaction_id = transaction_id
        self.name = name
    
    def __repr__(self):
        return f"name {self.name}"