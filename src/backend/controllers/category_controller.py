from services.category_service import CategoryService


class CategoryController:
    def __init__(self) -> None:
        self.category_service = CategoryService()

    def get_categories(self):
        return self.category_service.get_categories()

    def get_category(self, category_id):
        return self.category_service.get_category(category_id)

    def create_category(self, category: dict):
        return self.category_service.create_category(category)

    def update_category(self, category_id, category_data):
        return self.category_service.update_category(category_id, category_data)

    def delete_category(self, category_id):
        return self.category_service.delete_category(category_id)
