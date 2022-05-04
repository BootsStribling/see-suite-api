from datetime import datetime
from api.models.db import db

class Country(db.Model):
    __tablename__ = 'country'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)
    distributor_id = db.Column(db.Integer, db.ForeignKey('distributors.id'), nullable=False)

    def __init__(self, department_id, name, distributor_id):
        self.name = name
        self.distributor_id = distributor_id
        self.department_id = department_id
        
    def __repr__(self):
        return f"name {self.name}"