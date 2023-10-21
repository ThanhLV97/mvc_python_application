from datetime import datetime

from config.config import ProductStatus
from extensions import db
from sqlalchemy import func


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    image = db.Column(db.String(120), nullable=True)
    price = db.Column(db.Numeric, nullable=False)
    description = db.Column(db.String(), nullable=False)

    # Audit field
    created_date = db.Column(db.DateTime, nullable=True, default=datetime.now())
    updated_date = db.Column(db.DateTime, default=datetime.now, onupdate=func.now())

    # Relationship
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User")

    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=True)
    category = db.relationship("Category")

    @property
    def status(self):
        if self.stock > 0:
            return ProductStatus.AVAILABLE

        return ProductStatus.OUT_OF_STOCK

    def __repr__(self):
        return f"<Item {self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "category": self.category.to_dict(),
            "stock": self.stock,
            "price": self.price,
            "image": self.image,
            "description": self.description,
            "created_date": self.created_date,
            "updated_date": self.updated_date,
        }
