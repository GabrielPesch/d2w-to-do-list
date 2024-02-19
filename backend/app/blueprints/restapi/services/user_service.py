from ..validators.register_validator import validate_register
from ..validators.credentials_validator import validate_credentials
from ..repositories.user_repository import (
    create_user,
    generate_access_token,
    find_user_by_id,
)
from ..errors.error_factory import user_not_found_error
from ..helpers.make_response import make_success_response
from flask_jwt_extended import unset_jwt_cookies, create_access_token
from flask import jsonify


def register_service(name, email, password):
    validate_register(name, email, password)
    access_token = create_user(name=name, email=email, password=password)

    message = "User registered successfully"
    response = make_success_response(message=message, data=access_token)

    return response


def sign_in_service(email, password):
    user_id = validate_credentials(email, password)
    access_token = generate_access_token(user_id)

    message = "User signed in successfully"
    response = make_success_response(message=message, data=access_token)

    return response


def user_exists_by_id_or_throw(user_id):
    user = find_user_by_id(user_id)

    if user is None:
        user_not_found_error(id, user_id)

    return None


def log_out_service():
    message = "logout successful"
    unset_jwt_cookies(jsonify({"msg": message}))
    response = make_success_response(message)
    return response
