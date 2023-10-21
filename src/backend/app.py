from apis import api
from config.config import Config
from extensions import db, jwt, mgi
from flask import Flask, jsonify
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended.exceptions import NoAuthorizationError
from repositories.auth_repository import AuthenRepository
from repositories.user_repository import UserRepository
from utils.cli import assign_role, init_db

app = Flask(__name__)
app.config.from_object(Config)

with app.app_context():
    db.init_app(app)
    mgi.init_app(app, db)
    api.init_app(app)
    jwt.init_app(app)

    # Add cli
    app.cli.add_command(init_db)
    app.cli.add_command(assign_role)

    @app.before_request
    def before_request_handler():
        try:
            verify_jwt_in_request(optional=True, fresh=False, refresh=True, verify_type=False)
        except NoAuthorizationError:
            return jsonify({"message": "Missing Authorization Header"}), 401

    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user if isinstance(user, int) else user.id

    @jwt.user_lookup_loader
    def load_user(jwt_headers, jwt_payload):
        user_id = jwt_payload[app.config.get("JWT_IDENTITY_CLAIM")]
        return UserRepository.get_user(user_id)

    @jwt.expired_token_loader
    def expired_token_callback(expired_token, request):
        return jsonify({"message": "Token has expired"}), 401

    @jwt.token_in_blocklist_loader
    def check_if_token_revoked(jwt_headers, jwt_payload):
        try:
            return AuthenRepository.is_token_revoked(jwt_payload)
        except Exception:
            return True

    @api.errorhandler(NoAuthorizationError)
    def handle_no_authorization_error(error):
        return {"message": "Missing Authorization Header"}, 401

if __name__ == "__main__":
    app.run(debug=True)
