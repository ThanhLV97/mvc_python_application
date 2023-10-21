from extensions import api

from .resources.auth import api as auth_ns
from .resources.category import api as category_ns
from .resources.product import api as product_ns
from .resources.user import api as user_ns

api.add_namespace(user_ns)
api.add_namespace(auth_ns)
api.add_namespace(category_ns)
api.add_namespace(product_ns)
