from ..errors.error_factory import (
    field_min_size_error,
    field_max_size_error,
    entity_not_found_error,
    user_not_found_error,
    missing_field_error,
)
from ..repositories.task_repository import find_one_by_id
from ..repositories.user_repository import find_user_by_id
from ..repositories.category_repository import find_category_by_id


def validate_title(field, value):
    if value is None:
        return missing_field_error(field)
    TITLE_MIN_SIZE = 3
    if len(value) < TITLE_MIN_SIZE:
        return field_min_size_error(field, TITLE_MIN_SIZE)
    TITLE_MAX_SIZE = 50

    if len(value) > TITLE_MAX_SIZE:
        return field_max_size_error(TITLE_MAX_SIZE)

    return None


def validate_description(field, value):
    if value is None:
        return None

    DESCRIPTION_MAX_SIZE = 500
    if len(value) > DESCRIPTION_MAX_SIZE:
        return field_max_size_error(field, DESCRIPTION_MAX_SIZE)


def validate_user(user_id):
    if user_id is None:
        return user_not_found_error

    user = find_user_by_id(user_id)

    if user is None:
        return user_not_found_error

    return None


def validate_task(task_id, user_id):
    if task_id is None:
        return entity_not_found_error()

    task = find_one_by_id(task_id, user_id)

    if task is None:
        return entity_not_found_error()

    return None


def validate_category_id(category_id):
    if category_id is None:
        return None

    category = find_category_by_id(category_id)

    if category is None:
        return entity_not_found_error()


def validate_update_task(user_id, task_id, update_payload, category_id):
    data = {}

    if (
        not ("title" in update_payload)
        and not ("description" in update_payload)
        and not ("category_id" in update_payload)
    ):
        return missing_field_error()

    if "title" in update_payload:
        title = update_payload.get("title")
        validate_title("title", title)
        data["title"] = title

    if "description" in update_payload:
        description = update_payload.get("description")
        validate_description("description", description)
        data["description"] = description

    if "category_id" in update_payload:
        category_id = update_payload.get("category_id")
        validate_category_id(category_id)
        data["category_id"] = category_id

    validate_user(user_id)
    validate_task(task_id, user_id)

    return data
