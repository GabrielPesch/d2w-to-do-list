from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user_model import User
from .task_model import Task
from .category_model import Category
