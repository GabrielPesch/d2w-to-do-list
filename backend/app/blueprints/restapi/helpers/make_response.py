def make_success_response(message=None, data=None, pagination=None):
    response = {"success": True}

    if message is not None:
        response["message"] = message

    if data is not None:
        response["data"] = data

    if pagination is not None:
        response["pagination"] = {
            "total_pages": pagination.get("total_pages"),
            "current_page": pagination.get("current_page"),
            "per_page": pagination.get("per_page"),
        }

    return response
