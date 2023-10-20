from flask import jsonify, make_response


def create_response(data=None, message="Success", status_code=200):
    response = {
        "data": data,
        "message": message,
    }
    return make_response(jsonify(response), status_code)
