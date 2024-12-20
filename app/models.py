from datetime import datetime
from app import db

class Location(db.Model):
    __tablename__ = 'locations'
    uuid = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, uuid, name, created_at=None):
        self.uuid = uuid
        self.name = name
        if created_at is None:
            created_at = datetime.utcnow()
        self.created_at = created_at