from ..errors.error_factory import (
    invalid_field_type_error,
    field_min_size_error,
    entity_not_found_error,
)
from ..repositories.category_repository import find_many_by_ids


def validate_categories(category_ids):
    if category_ids is None:
        return None

    if not all(isinstance(id, int) for id in category_ids):
        return invalid_field_type_error("category_ids", "list of integers")

    CATEGORY_ID_MIN_VALUE = 1
    if any(id < CATEGORY_ID_MIN_VALUE for id in category_ids):
        return field_min_size_error("category_ids", CATEGORY_ID_MIN_VALUE)

    categories = find_many_by_ids(category_ids)
    if len(categories) != len(category_ids):
        return entity_not_found_error()

    return None


def validate_completed(completed):
    if completed is None:
        return None

    if not isinstance(completed, bool):
        return invalid_field_type_error("completed", "boolean")

    return None


def validate_filters(category_ids, completed):
    validate_categories(category_ids)
    validate_completed(completed)
    return None
