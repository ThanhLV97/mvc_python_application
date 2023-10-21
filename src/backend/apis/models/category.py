from extensions import api
from flask_restx import fields

category_model = api.model(
    "CategoryModel", {"id": fields.Integer, "name": fields.String}
)

creating_category_model = api.model("CategoryModel", {"name": fields.String})
