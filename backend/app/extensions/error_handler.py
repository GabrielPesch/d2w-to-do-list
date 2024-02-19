from flask import jsonify
from ..blueprints.restapi.errors.create_error import CustomError


def handle_custom_errors(error):
    error_message = str(error)
    error_type = error.error_type
    http_status = error.http_status

    response_data = {
        "success": False,
        "error": {"message": error_message, "type": error_type, "status": http_status},
    }

    response = jsonify(response_data)
    response.status_code = http_status
    return response


def init_app(app):
    app.errorhandler(CustomError)(handle_custom_errors)
