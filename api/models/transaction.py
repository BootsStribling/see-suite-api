from datetime import datetime
from api.models.db import db

class Transaction(db.Model):
  __tablename__='transactions'
  id = db.Column(db.Integer, primary_key=True)
  sellers_name = db.Column(db.String(100), nullable=False)
  buyers_name = db.Column(db.String(100), nullable=False)
  location_id = db.Column(db.String(100))
  transaction_total = db.Column(db.Float) 
  date = db.Column(db.String(100))
  sale_type = db.Column(db.String(100), nullable=False)
  

  def __init__(self, sellers_name, buyers_name, location_id, transaction_total, date, sale_type):
        self.sellers_name = sellers_name
        self.buyers_name = buyers_name
        self.location_id = location_id
        self.transaction_total = transaction_total
        self.date = date
        self.sale_type = sale_type

  def __repr__(self):
      return f"sellers_name {self.sellers_name}"

  def serialize(self):
    transaction = {c.name: getattr(self, c.name) for c in self.__table__.columns}
    print(transaction, 'transaction serialize triggered')
    return transaction

