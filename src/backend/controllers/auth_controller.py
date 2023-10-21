from flask import Response, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
from services.auth_service import AuthenService
from werkzeug.security import check_password_hash


class AuthController:
    def __init__(self) -> None:
        self.authen_service = AuthenService()

    def login(self, username: str, password: str):
        return self.authen_service.login(username, password)

    def register(self, username: str, password: str, email: str):
        return self.authen_service.register(username, password, email)

    def refresh(self, identity: str) -> Response:
        return self.authen_service.refresh(identity)

    def revoke_token(self, token_jti: str, user_id: int):
        return self.authen_service.revoke_token(token_jti, user_id)
