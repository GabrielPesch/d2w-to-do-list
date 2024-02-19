from flask import Blueprint

main = Blueprint("main", __name__)
session = Blueprint("session", __name__, url_prefix="/api/v1/session")
task = Blueprint("user", __name__, url_prefix="/api/v1/tasks")
category = Blueprint("category", __name__, url_prefix="/api/v1/categories")
