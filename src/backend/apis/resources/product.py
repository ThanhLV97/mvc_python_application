from apis.fields.product_field import creating_product_model
from controllers.product_controller import ProductController
from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restx import Namespace, Resource, inputs, reqparse

authorizations = {"Token": {"type": "apiKey", "in": "header", "name": "Authorization"}}

api = Namespace("products", description="product operations", authorizations=authorizations)
product_controller = ProductController()


@api.route("/product")
class ProductResouce(Resource):
    @jwt_required()
    @api.doc(security="Token")
    @api.expect(creating_product_model)
    def post(self):
        product = request.get_json()
        product["user_id"] = get_jwt_identity()

        return product_controller.create_product(product)


@api.route("/")
class ProductsResource(Resource):
    @jwt_required()
    @api.doc(security="Token", params={'page': 'Page', 'limit': 'limit'})
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=inputs.int_range(1, 99999), required=False, default=1, location='args')
        parser.add_argument('limit', type=inputs.int_range(1, 100), required=False, default=20, location='args')

        args = parser.parse_args()
        return product_controller.get_products(page=args['page'], per_page=args['limit'])


@api.route("/<int:product_id>")
class SingleproductResouce(Resource):
    def get(self, product_id):
        return product_controller.get_product(product_id)

    @api.expect(creating_product_model)
    def put(self, product_id):
        product = request.get_json()
        return product_controller.update_product(product_id, product)

    def delete(self, product_id):
        return product_controller.delete_product(product_id)
