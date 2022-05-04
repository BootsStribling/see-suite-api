from datetime import datetime
from api.models.db import db

class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    community_id = db.Column(db.Integer, db.ForeignKey('communities.id'), nullable=False)
    name = db.Column(db.String(100))

    def __init__(self, community_id, name):
        self.community_id = community_id
        self.name = name
    
    def __repr__(self):
        return f"name {self.name}"