import re
from ..repositories.user_repository import find_user_by_email
from ..errors.error_factory import (
    missing_field_error,
    invalid_email_error,
    invalid_field_type_error,
    field_min_size_error,
    field_max_size_error,
    email_already_registered_error,
)


def validate_name(field, value):
    if value is None:
        return missing_field_error(field)

    NAME_MIN_SIZE = 2
    if len(value) < NAME_MIN_SIZE:
        return field_min_size_error(field, NAME_MIN_SIZE)

    NAME_MAX_SIZE = 254
    if len(value) > NAME_MAX_SIZE:
        return field_max_size_error(NAME_MAX_SIZE)


def validate_email(field, value):
    if value is None:
        return missing_field_error(field)

    EMAIL_MIN_SIZE = 4
    if len(value) < EMAIL_MIN_SIZE:
        return field_min_size_error(field, EMAIL_MIN_SIZE)

    EMAIL_MAX_SIZE = 254
    if len(value) > EMAIL_MAX_SIZE:
        return field_max_size_error(field, EMAIL_MAX_SIZE)

    email_regex = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(email_regex, value):
        return invalid_email_error(value)

    user_registered = find_user_by_email(value)
    if user_registered:
        return email_already_registered_error(value)

    return None


def validate_password(field, value):
    if value is None:
        return missing_field_error(field)

    if not isinstance(value, str):
        return invalid_field_type_error(field, "string")

    PASSWORD_MIN_SIZE = 8
    if len(value) < PASSWORD_MIN_SIZE:
        return field_min_size_error(field, PASSWORD_MIN_SIZE)

    PASSWORD_MAX_SIZE = 100
    if len(value) > PASSWORD_MAX_SIZE:
        return field_max_size_error(field, PASSWORD_MAX_SIZE)

    return None


def validate_register(name, email, password):
    validate_password("Password", password)
    validate_email("Email", email)
    validate_name("Name", name)

    return None
