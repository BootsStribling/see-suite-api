from datetime import datetime
from api.models.db import db

class Global(db.Model):
    __tablename__ = 'global'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)

    def __init__(self, country_id, name):
        self.country_id = country_id
        self.name = name
    
    def __repr__(self):
        return f"name {self.name}"