from typing import List, Optional

from extensions import db
from models.category_model import Category
from sqlalchemy.exc import SQLAlchemyError


class CategoryRepository:
    @staticmethod
    def get_categories() -> List[Category]:
        categories = Category.query.all()
        return [category.to_dict() for category in categories]

    @staticmethod
    def get_category(category_id) -> Optional[dict]:
        category = Category.query.get(category_id)
        return category.to_dict() if category else None

    @staticmethod
    def create_category(category: dict) -> dict:
        category = Category(name=category.get("name"))
        db.session.add(category)
        db.session.commit()
        return category.to_dict()

    @staticmethod
    def update_category(category_id, updated_category) -> Category:
        try:
            category = Category.query.get(category_id)
            for key, value in updated_category.items():
                setattr(category, key, value)
            db.session.commit()
            return category.to_dict()
        except SQLAlchemyError:
            db.session.rollback()
            raise

    @staticmethod
    def delete_category(category_id) -> bool:
        try:
            category = Category.query.get(category_id)
            db.session.delete(category)
            db.session.commit()
            return category.to_dict()
        except SQLAlchemyError:
            db.session.rollback()
            raise

    @staticmethod
    def get_category_by_name(name) -> Optional[Category]:
        return Category.query.filter_by(name=name).first()
