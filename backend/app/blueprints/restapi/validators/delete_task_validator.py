from ..errors.error_factory import (
    entity_not_found_error,
    user_not_found_error,
)
from ..repositories.task_repository import find_one_by_id
from ..repositories.user_repository import find_user_by_id


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


def validate_delete_task(task_id, user_id):
    validate_user(user_id)
    validate_task(task_id, user_id)
