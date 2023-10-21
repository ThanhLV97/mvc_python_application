from datetime import datetime

from extensions import db
from sqlalchemy import func


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    
    # Audit field
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_date = db.Column(db.DateTime, default=datetime.now, onupdate=func.now())

    def __repr__(self):
        return f"<Category {self.name}>"

    def to_dict(self):
        return {"id": self.id, "name": self.name}