from .create_error import create_error_response
from .error_dictionary import ERROR_DICT


def custom_error_response(error_type, http_status, additional_info=None):
    additional_info = additional_info or {}
    message_template = ERROR_DICT.get(error_type, "An error occurred")

    return create_error_response(
        error_type,
        http_status,
        message_template.format(**additional_info),
    )


def missing_field_error(field):
    return custom_error_response(
        "missing_field_error", 400, additional_info={"field": field}
    )


def invalid_email_error(email):
    return custom_error_response(
        "invalid_email_error", 400, additional_info={"email": email}
    )


def invalid_field_type_error(field, field_type):
    return custom_error_response(
        "invalid_type_error",
        400,
        field,
        additional_info={"field": field, "field_type": field_type},
    )


def field_min_size_error(field, min_size):
    return custom_error_response(
        "field_min_size_error",
        400,
        additional_info={"field": field, "min_size": min_size},
    )


def field_max_size_error(field, max_size):
    return custom_error_response(
        "field_max_size_error",
        400,
        additional_info={"field": field, "max_size": max_size},
    )


def email_already_registered_error(email):
    return custom_error_response(
        "email_already_registered_error",
        400,
        additional_info={
            "email": email,
        },
    )


def invalid_credentials_error():
    return custom_error_response("invalid_credentials_error", 401, additional_info={})


def user_not_found_error(field, value):
    return custom_error_response(
        "user_not_found_error", 404, additional_info={"field": field, "value": value}
    )


def field_must_be_positive_error(field):
    return custom_error_response(
        "field_must_be_positive_error",
        400,
        additional_info={"field": field},
    )


def field_must_be_lower_than_error(field, value):
    return custom_error_response(
        "field_must_be_lower_than_error",
        400,
        additional_info={"field": field, "value": value},
    )


def entity_not_found_error():
    return custom_error_response("entity_not_found_error", 404, additional_info={})


def unauthorized_error():
    return custom_error_response("unauthorized_error", 403, additional_info={})
