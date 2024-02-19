from app.models.category_model import Category
from app.models.model import db


def find_category_by_id(category_id):
    category = Category.query.filter(
        Category.deleted_at.is_(None), Category.id == category_id
    ).first()

    if category:
        return category

    return None


def find_all():
    categories = Category.query.filter(Category.deleted_at.is_(None))

    serialized_categories = []

    for category in categories:
        serialized_category = category.as_dict()
        serialized_categories.append(serialized_category)

    return serialized_categories


def find_many_by_ids(category_ids):
    categories = Category.query.filter(
        Category.id.in_(category_ids), Category.deleted_at.is_(None)
    ).all()

    serialized_categories = []

    for category in categories:
        serialized_category = category.as_dict()
        serialized_categories.append(serialized_category)

    return serialized_categories
