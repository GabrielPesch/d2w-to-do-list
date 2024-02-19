from ..errors.error_factory import (
    missing_field_error,
    field_min_size_error,
    field_max_size_error,
    user_not_found_error,
    entity_not_found_error,
)
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
        return field_max_size_error(field, TITLE_MAX_SIZE)

    return None


def validate_description(field, value):
    if value is None:
        return None

    DESCRIPTION_MAX_SIZE = 500
    if len(value) > DESCRIPTION_MAX_SIZE:
        return field_max_size_error(field, DESCRIPTION_MAX_SIZE)


def validate_category_id(field, value):
    if value is None:
        return missing_field_error(field)

    category = find_category_by_id(value)

    if category is None:
        return entity_not_found_error()


def validate_user(user_id):
    if user_id is None or not str(user_id).isdigit():
        return user_not_found_error("id", user_id)

    user = find_user_by_id(user_id)
    if user is None:
        return user_not_found_error("id", user_id)
    return None


def validate_create_task(user_id, title, description, category_id):
    validate_title("title", title)
    validate_category_id("category_id", category_id)
    validate_description("description", description)
    validate_user(user_id)

    return None
