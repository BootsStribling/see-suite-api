from datetime import datetime
from pickle import FALSE
from api.models.db import db

class Transaction(db.Model):
  __tablename__='transactions'
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.String(100))
  sale_type = db.Column(db.String(100), nullable=False)
  transaction_total = db.Column(db.Float, nullable = False)
  community_id = db.Column(db.Integer, nullable=False)
  manager = db.Column(db.String(1), nullable=FALSE)
  department_id = db.Column(db.Integer, nullable=False)
  country_id = db.Column(db.Integer, nullable=False)
  distributor = db.Column(db.Integer, nullable=False)
  

  def __init__(self, transaction_total, date, sale_type, community_id, manager, department_id, country_id, distributor):
        self.date = date
        self.sale_type = sale_type
        self.transaction_total = transaction_total
        self.community_id = community_id
        self.manager = manager
        self.department_id = department_id
        self.country_id = country_id
        self.distributor = distributor

  def __repr__(self):
      return f"sellers_name {self.sellers_name}"

  def serialize(self):
    transaction = {c.name: getattr(self, c.name) for c in self.__table__.columns}
    print(transaction, 'transaction serialize triggered')
    return transaction

