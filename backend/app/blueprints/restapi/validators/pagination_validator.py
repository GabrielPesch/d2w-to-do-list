from ..errors.error_factory import (
    missing_field_error,
    field_must_be_positive_error,
    field_must_be_lower_than_error,
)


def validate_page(field, value):
    if value is None:
        return None

    PAGE_MIN_VALUE = 1
    if not isinstance(value, int) or value < PAGE_MIN_VALUE:
        return field_must_be_positive_error(field)

    return None


def validate_per_page(field, value):
    if value is None:
        return missing_field_error(field)

    PER_PAGE_MIN_VALUE = 1
    if not isinstance(value, int) or value < PER_PAGE_MIN_VALUE:
        return field_must_be_positive_error(field)

    PER_PAGE_MAX_VALUE = 100
    if value > PER_PAGE_MAX_VALUE:
        return field_must_be_lower_than_error(field, PER_PAGE_MAX_VALUE)
    return None


def validate_pagination(page, per_page):
    validate_page("page", page)
    validate_per_page("per_page", per_page)
