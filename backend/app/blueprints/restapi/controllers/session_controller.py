from flask import request, jsonify
from ..controllers import session
from ..services.user_service import (
    register_service,
    sign_in_service,
    log_out_service,
)


@session.route("/sign_in", methods=["POST"])
def sign_in():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    response = sign_in_service(email, password)
    return jsonify(response), 200


@session.route("/sign_up", methods=["POST"])
def sign_up():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    response = register_service(name, email, password)

    return jsonify(response), 201


@session.route("/sign_out", methods=["POST"])
def logout():
    response = log_out_service()
    return response
