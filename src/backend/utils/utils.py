from flask import jsonify, make_response
from flask_sqlalchemy.pagination import Pagination


def create_response(data=None, message="Success", status_code=200):
    if isinstance(data, Pagination):
        response = {
            'data': [item.to_dict() for item in data.items],
            'total': data.total,
            'page': data.page,
            'limit': data.per_page,
            'has_more': data.has_next,
            'message': message,
        }

    else:
        response = {
            'data': data,
            'message': message,
        }

    return make_response(jsonify(response), status_code)
