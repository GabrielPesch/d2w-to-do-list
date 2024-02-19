from ..validators.create_task_validator import validate_create_task
from ..validators.pagination_validator import validate_pagination
from ..repositories.task_repository import (
    create_task,
    find_all_tasks_by_user_id,
    find_one_by_id,
    handle_task_complete_by_id,
    update_task,
    remove_task,
)
from ..validators.update_task_validator import validate_update_task
from ..validators.delete_task_validator import validate_delete_task
from ..validators.find_all_tasks_validator import validate_filters
from ..errors.error_factory import entity_not_found_error
from ..helpers.make_response import make_success_response


def create_task_service(current_user_id, title, description, category_id):
    validate_create_task(current_user_id, title, description, category_id)
    task = create_task(current_user_id, title, description, category_id)
    message = "task created successfully"
    response = make_success_response(message=message, data=task)

    return response


def find_all_by_user_id(
    user_id,
    category_ids,
    completed,
    page=1,
    per_page=10,
):
    validate_pagination(page, per_page)
    validate_filters(category_ids, completed)
    paginated_tasks = find_all_tasks_by_user_id(
        user_id, page, per_page, category_ids, completed
    )
    data = paginated_tasks.get("tasks", [])
    pagination = {
        "total_pages": paginated_tasks.get("total_pages", 0),
        "current_page": paginated_tasks.get("current_page", 0),
        "per_page": paginated_tasks.get("per_page", 0),
        "categories": category_ids,
    }

    response = make_success_response(data=data, pagination=pagination)
    return response


def find_one(task_id, user_id):
    task = find_one_by_id(task_id, user_id)
    if task is None:
        return entity_not_found_error()
    print(task)

    response = make_success_response(data=task)
    return response


def handle_task_complete(task_id, user_id):
    handle_task_complete_by_id(task_id, user_id)
    response = make_success_response()
    return response


def update_task_by_id(user_id, task_id, update_payload, category_id):
    update_payload = validate_update_task(
        user_id=user_id,
        task_id=task_id,
        update_payload=update_payload,
        category_id=category_id,
    )

    updated_task = update_task(task_id=task_id, update_payload=update_payload)
    response = make_success_response(data=updated_task)
    return response


def delete_task(task_id, user_id):
    validate_delete_task(task_id, user_id)
    remove_task(task_id, user_id)

    response = make_success_response()
    return response
