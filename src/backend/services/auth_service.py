from flask import Response, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
from repositories.auth_repository import AuthenRepository
from repositories.user_repository import UserRepository
from utils.utils import create_response
from werkzeug.security import check_password_hash, generate_password_hash


class AuthenService():
    def login(self, username: str, password: str):
        user = UserRepository.get_user_by_username(username)
        if not user:
            return {"error": "User does not exist"}, 401

        if not check_password_hash(user.password_hash, password):
            return {"error": "Incorrect password"}, 401

        access_token=create_access_token(user)
        refresh_token=create_refresh_token(user)

        AuthenRepository.add_token(access_token)
        AuthenRepository.add_token(refresh_token)

        return jsonify(
            access_token=access_token,
            refresh_token=refresh_token,
        )

    def register(self, username: str, password: str, email: str):
        exist_user = UserRepository.get_user_by_username_or_email(username, email)

        if exist_user:
            return create_response(message="User already exist", status_code=404)

        user = {
            'username': username,
            'email': email,
            'password_hash': generate_password_hash(password)
        }

        created_user = UserRepository.create_user(user=user)

        return create_response(data=created_user)

    def refresh(self, identity: str) -> Response:
        access_token = create_access_token(identity)

        AuthenRepository.add_token(access_token)

        return jsonify(access_token=access_token)

    def revoke_token(self, token_jti, user_id):
        try:
            AuthenRepository.revoke_token(token_jti, user_id)
            return create_response(message="Token revocation is successful")
        except Exception:
            return create_response(message="Token revocation is fail")
