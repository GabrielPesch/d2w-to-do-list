from typing import Dict, Tuple
from .error_dictionary import ERROR_DICT


class CustomError(Exception):

    def __init__(
        self,
        error_type="Internal Server Error",
        http_status=500,
        message="The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.",
        additional_info=None,
    ):
        super().__init__(message)
        self.error_type = error_type
        self.http_status = http_status
        self.additional_info = additional_info or {}


def create_error_response(
    error_type: str, http_status: int, message: str, additional_info=None
) -> Tuple[Dict[str, str], int]:
    raise CustomError(error_type, http_status, message, additional_info)
