from typing import List, Optional

from extensions import db
from models.product_model import Product
from sqlalchemy import and_
from sqlalchemy.exc import SQLAlchemyError


class ProductRepository:
    @staticmethod
    def get_products() -> List[Product]:
        products = Product.query.all()
        return [product.to_dict() for product in products]

    @staticmethod
    def get_product(product_id: int) -> Optional[dict]:
        product = Product.query.get(product_id)
        return product.to_dict() if product else None

    @staticmethod
    def create_product(product: dict) -> dict:
        product = Product(
            name=product.get("name"),
            stock=product.get("stock"),
            image=product.get("image"),
            price=product.get("price"),
            description=product.get("description"),
            user_id=product.get("user_id"),
            category_id=product.get("category_id"),
        )

        db.session.add(product)
        db.session.commit()
        return product.to_dict()

    @staticmethod
    def update_product(product_id, updated_product) -> Product:
        try:
            product = Product.query.get(product_id)

            for key, value in updated_product.Products():
                setattr(product, key, value)

            db.session.commit()
            return product.to_dict()

        except SQLAlchemyError:
            db.session.rollback()
            raise

    @staticmethod
    def delete_product(product_id) -> bool:
        try:
            product = Product.query.get(product_id)
            db.session.delete(product)
            db.session.commit()
            return product.to_dict()
        except SQLAlchemyError:
            db.session.rollback()
            raise

    @staticmethod
    def get_product_by_name_and_category(
        name: str, category_id: str
    ) -> Optional[Product]:
        return Product.query.filter(
            and_(
                Product.name == name,
                Product.category_id == category_id
            ),
        ).first()

    @staticmethod
    def get_product_by_name(name) -> Optional[Product]:
        return Product.query.filter_by(name=name).first()

    @staticmethod
    def get_products_by_user(user_id) -> List[Product]:
        products = Product.query.filter_by(user_id=user_id).all()
        return [product.to_dict() for product in products]

    @staticmethod
    def update_stock(product_id: int, new_stock: int) -> None:
        product = Product.query.get(product_id)
        try:
            product.stock = new_stock
            db.session.add(product)
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise
