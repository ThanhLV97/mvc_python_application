from services.product_service import ProductService


class ProductController:
    def __init__(self) -> None:
        self.product_service = ProductService()

    def get_products(self, page: int, per_page: int):
        return self.product_service.get_products(page, per_page)

    def get_product(self, product_id):
        return self.product_service.get_product(product_id)

    def create_product(self, product: dict):
        return self.product_service.create_product(product)

    def update_product(self, product_id, product_data):
        return self.product_service.update_product(product_id, product_data)

    def delete_product(self, product_id):
        return self.product_service.delete_product(product_id)

    def get_products_by_user(self, user_id):
        return self.product_service.get_products_by_user(user_id)
