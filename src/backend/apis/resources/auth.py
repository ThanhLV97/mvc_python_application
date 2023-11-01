from apis.fields.user_field import creating_user_model, login_model
from controllers.auth_controller import AuthController
from flask_jwt_extended import get_jwt, get_jwt_identity, jwt_required
from flask_restx import Namespace, Resource

api = Namespace("auth", description="Authentication operations")
auth_controller = AuthController()


@api.route("/login")
class Login(Resource):
    @api.expect(login_model, validate=True)
    def post(self):
        return auth_controller.login(api.payload["username"], api.payload["password"])


@api.route("/register")
class Register(Resource):
    @api.expect(creating_user_model, validate=True)
    def post(self):
        return auth_controller.register(api.payload["username"], api.payload["password"], email=api.payload["email"])


@api.route("/refresh")
class Refresh(Resource):
    @jwt_required(refresh=True)
    @api.doc(security="Token")
    def post(self):
        identity = get_jwt_identity()
        return auth_controller.refresh(identity)


@api.route("/revoke_access")
class AccessTokenRevocation(Resource):
    @jwt_required()
    @api.doc(security="Token")
    def delete(self):
        jti = get_jwt()["jti"]
        user_id = get_jwt_identity()
        auth_controller.revoke_token(jti, user_id)
        return {"msg": "Access token is revoked"}, 200


@api.route("/revoke_access")
class RefreshTokenRevocation(Resource):
    @jwt_required(refresh=True)
    @api.doc(security="Token")
    def delete(self):
        jti = get_jwt()["jti"]
        user_id = get_jwt_identity()
        auth_controller.revoke_token(jti, user_id)
        return {"msg": "Refresh token is revoked"}, 200
