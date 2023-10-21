from extensions import api

from .resources.auth import api as auth_ns
from .resources.user import api as user_ns

api.add_namespace(user_ns)
api.add_namespace(auth_ns)
