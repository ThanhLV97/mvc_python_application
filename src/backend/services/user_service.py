from repositories.user_repository import UserRepository
from utils.utils import create_response
from werkzeug.security import generate_password_hash


class UserService:
    def get_users(self):
        users = UserRepository.get_users()
        return create_response(data=users)

    def get_user(self, user_id):
        user = UserRepository.get_user(user_id=user_id)
        if not user:
            return create_response(message="User not found", status_code=404)

        return create_response(data=user)

    def create_user(self, user: dict):
        exist_user = UserRepository.get_user_by_username_or_email(
            user.get("username"), user.get("email")
        )

        if exist_user:
            return create_response(message="User already exist", status_code=404)

        user["password_hash"] = generate_password_hash(user.get("password"))
        created_user = UserRepository.create_user(user=user)
        return create_response(data=created_user)

    def update_user(self, user_id, user_data):
        user = UserRepository.get_user(user_id)
        if not user:
            return create_response(message="User not found", status_code=404)

        updated_user = UserRepository.update_user(user_id, user_data)
        if updated_user:
            return create_response(data=updated_user)

        return create_response(message="Failed to update user")

    def delete_user(self, user_id):
        user = UserRepository.get_user(user_id)

        if not user:
            return create_response(message="User not found", status_code=404)

        deleted = UserRepository.delete_user(user_id)
        if deleted:
            return create_response(message="User deleted successfully")
        else:
            return create_response(message="Failed to delete user")
