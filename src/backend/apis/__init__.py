from extensions import api

from .resources.user import api as user_ns

api.add_namespace(user_ns)
