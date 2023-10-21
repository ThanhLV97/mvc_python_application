from repositories.category_repository import CategoryRepository
from utils.utils import create_response


class CategoryService:
    def get_categories(self):
        categories = CategoryRepository.get_categories()
        return create_response(data=categories)

    def get_category(self, category_id):
        category = CategoryRepository.get_category(category_id)
        if not category:
            return create_response(message="Category not found", status_code=400)

        return create_response(data=category)

    def create_category(self, category: dict):
        if not category:
            return create_response(
                message="Failed to create new category ", status_code=404
            )

        exist_category = CategoryRepository.get_category_by_name(
            category.get("name", None)
        )

        if exist_category:
            return create_response(message="Category already exist", status_code=404)

        created_category = CategoryRepository.create_category(category)
        return create_response(data=created_category)

    def update_category(self, category_id, category):
        exist_category = CategoryRepository.get_category(category_id)
        if not exist_category:
            return create_response(message="category not found", status_code=404)

        updated_category = CategoryRepository.update_category(category_id, category)
        if updated_category:
            return create_response(data=updated_category)

        return create_response(message="Failed to update category")

    def delete_category(self, category_id):
        category = CategoryRepository.get_category(category_id)

        if not category:
            return create_response(message="category not found", status_code=404)

        deleted = CategoryRepository.delete_category(category_id)
        if deleted:
            return create_response(message="category deleted successfully")

        else:
            return create_response(message="Failed to delete category")
