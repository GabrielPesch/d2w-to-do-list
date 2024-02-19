from flask import jsonify
from ..controllers import category
from flask_jwt_extended import jwt_required
from ..services.categories_service import find_all_categories


@category.route("/", methods=["GET"])
@jwt_required()
def index():
    response = find_all_categories()
    return jsonify(response), 200
