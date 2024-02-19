from ..repositories.category_repository import find_all
from ..helpers.make_response import make_success_response


def find_all_categories():
    categories = find_all()

    response = make_success_response(data=categories)
    return response
