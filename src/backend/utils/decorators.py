from functools import wraps

from flask_jwt_extended import get_jwt_identity
from models.user_model import User


def role_required(role):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            user_id = get_jwt_identity()
            user = User.query.get(user_id)

            if role not in user.roles:
                return {'message': f'{role} permission is required'}, 403

            return fn(*args, **kwargs)

        return decorator

    return wrapper
