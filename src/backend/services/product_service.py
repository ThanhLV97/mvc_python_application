from repositories.category_repository import CategoryRepository
from repositories.product_repository import ProductRepository
from utils.utils import create_response


class ProductService:
    def get_products(self):
        products = ProductRepository.get_products()
        return create_response(data=products)

    def get_product(self, product_id):
        product = ProductRepository.get_product(product_id)
        if not product:
            return create_response(message="product not found", status_code=400)

        return create_response(data=product)

    def create_product(self, product: dict):
        if not product:
            return create_response(message="Failed to create product", status_code=404)

        category = CategoryRepository.get_category(product.get("category_id"))
        if not category:
            return create_response(message="Category is not found", status_code=404)

        exist_product = ProductRepository.get_product_by_name(
            product.get("name", None),
        )

        if exist_product:
            return create_response(message="product already exist", status_code=404)

        created_product = ProductRepository.create_product(product)
        return create_response(data=created_product)

    def update_product(self, product_id, product):
        exist_product = ProductRepository.get_product(product_id)
        if not exist_product:
            return create_response(message="product not found", status_code=404)

        category = CategoryRepository.get_category(product.get("category_id"))
        if not category:
            return create_response(message="Category is not found", status_code=404)

        updated_product = ProductRepository.update_product(product_id, product)
        if updated_product:
            return create_response(data=updated_product)

        return create_response(message="Failed to update product")

    def delete_product(self, product_id):
        product = ProductRepository.get_product(product_id)

        if not product:
            return create_response(message="product not found", status_code=404)

        deleted = ProductRepository.delete_product(product_id)
        if deleted:
            return create_response(message="product deleted successfully")

        else:
            return create_response(message="Failed to delete product")

    def get_products_by_user(self, user_id):
        products = ProductRepository.get_products_by_user(user_id)
        return create_response(data=products)
