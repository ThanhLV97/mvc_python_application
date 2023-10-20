from services.user_service import UserService


class UserController:
    def __init__(self) -> None:
        self.user_service = UserService()

    def get_users(self):
        return self.user_service.get_users()

    def get_user(self, user_id):
        return self.user_service.get_user(user_id)

    def create_user(self, user: dict):
        return self.user_service.create_user(user)

    def update_user(self, user_id, user_data):
        return self.user_service.update_user(user_id, user_data)

    def delete_user(self, user_id):
        return self.user_service.delete_user(user_id)
