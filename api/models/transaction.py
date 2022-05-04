from datetime import datetime
from api.models.db import db

class Transaction(db.model):
  __tablename__='transactions'
  id = db.Column(db.Integer, primary_key=True)
  sellers_name = db.Column(db.String(100), nullable=False)
  buyers_name = db.Column(db.String(100), nullable=False)
  location_id = db.Column(db.String(100))
  transaction_total = db.Column(db.Float) 
  date = db.Column(db.String(100))
  type = db.Column(db.String(100), nullable=False)
  communities = db.relationship('Community')

  def __init__(self, sellers_name, buyers_name, location_id, transaction_total, date, type, communities):
        self.sellers_name = sellers_name
        self.buyers_name = buyers_name
        self.location_id = location_id
        self.transaction_total = transaction_total
        self.date = date
        self.type = type

    def __repr__(self):
        return f"sellers_name {self.sellers_name}"

