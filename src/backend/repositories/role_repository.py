from typing import List, Optional

from extensions import db
from models.user_model import Role, User, UserRole


class RoleRepository:

    @staticmethod
    def get_all() -> List[Role]:
        return Role.query.all()

    @staticmethod
    def get_by_id(role_id: int) -> Optional[Role]:
        return Role.query.get(role_id)

    @staticmethod
    def get_by_name(name: str) -> Optional[Role]:
        return Role.query.filter_by(name=name).first()

    @staticmethod
    def get_by_slug(slug: str) -> Optional[Role]:
        return Role.query.filter_by(slug=slug).first()

    @staticmethod
    def create(name: str, slug: str) -> Role:
        role = Role(name=name, slug=slug)
        db.session.add(role)
        db.session.commit()
        return role

    @staticmethod
    def update(role: Role, name: str, slug: str) -> Role:
        role.name = name
        role.slug = slug
        db.session.commit()
        return role

    @staticmethod
    def delete(role: Role) -> None:
        db.session.delete(role)
        db.session.commit()

    @staticmethod
    def init_role() -> None:
        for role in ["Admin", "User"]:
            RoleRepository.create(role, role.lower())


class RoleUserRepository:

    @staticmethod
    def add_role_to_user(user: User, role: Role):
        user.roles.append(role)
        db.session.commit()

    @staticmethod
    def remove_role_from_user(user: User, role: Role):
        UserRole.query.filter_by(
            user_id=user.id,
            role_id=role.id
        ).delete()
        db.session.commit()

    @staticmethod
    def get_roles_for_user(user: User) -> List[Role]:
        return user.roles

    @staticmethod
    def get_users_for_role(role: Role) -> List[User]:
        return role.users
