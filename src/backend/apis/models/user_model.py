from extensions import api
from flask_restx import fields

login_model = api.model(
    "LoginModel", {"username": fields.String, "password": fields.String}
)

user_model = api.model("UserModel", {"id": fields.Integer, "username": fields.String})

creating_user_model = api.model(
    "UserModel",
    {"username": fields.String, "password": fields.String, "email": fields.String},
)
