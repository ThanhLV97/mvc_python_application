from apis.fields.user_field import creating_user_model
from controllers.user_controller import UserController
from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restx import Namespace, Resource
from utils.decorators import role_required

authorizations = {"Token": {"type": "apiKey", "in": "header", "name": "Authorization"}}

api = Namespace("users", description="User operations", authorizations=authorizations)
users_controller = UserController()


@api.route("/user")
class UserResource(Resource):
    @api.expect(creating_user_model)
    def post(self):
        user = request.get_json()
        return users_controller.create_user(user)


@api.route("/")
class UsersResource(Resource):
    @jwt_required()
    @role_required('admin')
    @api.doc(security="Token")
    def get(self):
        return users_controller.get_users()


@api.route("/<int:user_id>")
class SingleUserResource(Resource):
    def get(self, user_id):
        return users_controller.get_user(user_id)

    def put(self, user_id):
        user = request.get_json()
        return users_controller.update_user(user_id, user)

    def delete(self, user_id):
        return users_controller.delete_user(user_id)


@api.route("/me")
class MeResource(Resource):
    @jwt_required()
    @api.doc(security="Token")
    def get(self):
        return users_controller.get_user(get_jwt_identity())
