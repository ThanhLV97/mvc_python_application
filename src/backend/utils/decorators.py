import json
from functools import wraps

import redis
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity
from models.user_model import User

redis_client = redis.Redis(host='redis', port=6379)


def role_required(role):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            user_id = get_jwt_identity()
            user = User.query.get(user_id)

            if not user.has_role(role):
                return {'message': f'{role} permission is required'}, 403

            return fn(*args, **kwargs)

        return decorator

    return wrapper


def cache_response(timeout=300):
    def decorator(view_func):
        def wrapper(*args, **kwargs):
            # Generate a cache key based on the request URL
            cache_key = f'api:{request.url}'
            # Check if the response is already cached
            response = redis_client.get(cache_key)
            if response is not None:
                return jsonify(json.loads(response.decode()))

            # Execute the view function and cache the response
            result = view_func(*args, **kwargs)
            redis_client.setex(cache_key, timeout, result.data)

            return result

        return wrapper

    return decorator
