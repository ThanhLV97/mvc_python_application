from typing import List, Optional

from extensions import db
from models.user_model import User
from sqlalchemy import or_
from sqlalchemy.exc import SQLAlchemyError


class UserRepository:
    @staticmethod
    def get_users() -> List[User]:
        users = User.query.all()
        return [user.to_dict() for user in users]

    @staticmethod
    def get_user(user_id) -> Optional[dict]:
        user = User.query.get(user_id)
        return user.to_dict() if user else None

    @staticmethod
    def create_user(user: dict) -> dict:
        user = User(
            username=user.get("username"),
            email=user.get("email"),
            password_hash=user.get("password_hash"),
        )
        db.session.add(user)
        db.session.commit()
        return user.to_dict()

    @staticmethod
    def update_user(user_id, updated_data) -> User:
        try:
            user = User.query.get(user_id)
            for key, value in updated_data.items():
                setattr(user, key, value)
            db.session.commit()
            return user.to_dict()
        except SQLAlchemyError:
            db.session.rollback()
            raise

    @staticmethod
    def delete_user(user_id) -> bool:
        try:
            user = User.query.get(user_id)
            db.session.delete(user)
            db.session.commit()
            return user.to_dict()
        except SQLAlchemyError:
            db.session.rollback()
            raise

    @staticmethod
    def get_user_by_username_or_email(username, email) -> Optional[User]:
        return User.query.filter(
            or_(User.username == username, User.email == email)
        ).first()

    @staticmethod
    def get_user_by_username(username: str) -> Optional[User]:
        return User.query.filter_by(username=username).first()

    @staticmethod
    def get_user_by_email(email: str) -> Optional[User]:
        return User.query.filter_by(email=email).first()
