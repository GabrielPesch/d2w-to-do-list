from flask import request, jsonify
from ..controllers import task
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.task_service import (
    create_task_service,
    find_all_by_user_id,
    find_one,
    handle_task_complete,
    update_task_by_id,
    delete_task,
)
from ..errors.error_factory import entity_not_found_error


@task.route("/", methods=["POST"])
@jwt_required()
def create():
    data = request.get_json()

    current_user_id = get_jwt_identity()
    title = data.get("title")
    description = data.get("description")
    category_id = data.get("category_id")

    response = create_task_service(current_user_id, title, description, category_id)
    return jsonify(response), 201


@task.route("/", methods=["GET"])
@jwt_required()
def index():
    current_user_id = get_jwt_identity()

    print("user", current_user_id)

    category_ids = request.args.getlist("category_id", type=int)

    completed = request.args.get(
        "completed", default=None, type=lambda v: v.lower() == "true"
    )

    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=10, type=int)
    filter

    response = find_all_by_user_id(
        current_user_id,
        category_ids=category_ids,
        completed=completed,
        page=page,
        per_page=per_page,
    )

    return jsonify(response), 200


@task.route("/<int:task_id>", methods=["GET"])
@jwt_required()
def show(task_id: int):
    current_user_id = get_jwt_identity()

    response = find_one(task_id, current_user_id)
    return jsonify(response), 200


@task.route("/<int:task_id>", methods=["PATCH"])
@jwt_required()
def switch_complete_task(task_id: int):
    current_user_id = get_jwt_identity()

    response = handle_task_complete(task_id, current_user_id)
    return jsonify(response), 200


@task.route("/<int:task_id>", methods=["PUT"])
@jwt_required()
def update_task(task_id: int):
    current_user_id = get_jwt_identity()

    data = request.get_json()

    update_payload = {}

    if "title" in data:
        title = data.get("title")
        update_payload["title"] = title

    if "description" in data:
        description = data.get("description")
        update_payload["description"] = description

    if "category_id" in data:
        category_id = data.get("category_id")
        update_payload["category_id"] = category_id

    if "title" in data or "description" in data or "category_id" in data:
        response = update_task_by_id(
            current_user_id, task_id, update_payload, category_id
        )
        return jsonify(response), 200

    return entity_not_found_error()


@task.route("/<int:task_id>", methods=["DELETE"])
@jwt_required()
def soft_delete_task(task_id: int):
    current_user_id = get_jwt_identity()

    response = delete_task(task_id, current_user_id)
    return jsonify(response), 200
