from apis.fields.category_field import creating_category_model
from controllers.category_controller import CategoryController
from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource
from utils.decorators import cache_response, role_required

authorizations = {"Token": {"type": "apiKey", "in": "header", "name": "Authorization"}}

api = Namespace(
    "categories", description="category operations", authorizations=authorizations
)
category_controller = CategoryController()


@api.route("/category")
class CategotyResource(Resource):
    @api.expect(creating_category_model)
    @role_required('admin')
    def post(self):
        category = request.get_json()
        return category_controller.create_category(category)


@api.route("/")
class CategoriesResource(Resource):
    @api.doc(security="Token")
    @jwt_required()
    @cache_response(timeout=60)
    def get(self):
        return category_controller.get_categories()


@api.route("/<int:category_id>")
class SingleCategoryResource(Resource):
    def get(self, category_id):
        return category_controller.get_category(category_id)

    @api.expect(creating_category_model)
    @role_required('admin')
    def put(self, category_id):
        user = request.get_json()
        return category_controller.update_category(category_id, user)

    @role_required('admin')
    def delete(self, category_id):
        return category_controller.delete_category(category_id)
