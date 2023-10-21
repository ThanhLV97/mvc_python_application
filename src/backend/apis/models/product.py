from extensions import api
from flask_restx import fields

product_model = api.model("ProductModel", {"id": fields.Integer, "name": fields.String})

creating_product_model = api.model(
    "ProductModel",
    {
        "name": fields.String,
        "image": fields.String,
        "stock": fields.Integer,
        "price": fields.Float,
        "category_id": fields.Integer,
        "description": fields.String,
    },
)
