from extensions import api
from flask_restx import fields

login_model = api.model(
    "LoginModel", {
        "username": fields.String(required=True),
        "password": fields.String(required=True)
    }
)

user_model = api.model("UserModel", {"id": fields.Integer, "username": fields.String})

creating_user_model = api.model(
    "UserModel", {
        "username": fields.String(required=True),
        "password": fields.String(required=True),
        "email": fields.String(required=True)},
)
