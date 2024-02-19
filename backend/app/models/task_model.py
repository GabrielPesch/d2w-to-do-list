from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from .model import db
from datetime import datetime
from typing import List, TypedDict
from sqlalchemy import DateTime
import pytz


def current_time():
    sao_paulo_tz = pytz.timezone("America/Sao_Paulo")
    return datetime.now(sao_paulo_tz)


class TaskDict(TypedDict):
    id: int
    title: str
    description: str
    completed: bool
    user_id: int
    category_id: int


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, ForeignKey("user.id"))
    category_id = db.Column(db.Integer, ForeignKey("category.id"))
    created_at = db.Column(DateTime, default=current_time)
    updated_at = db.Column(DateTime, onupdate=current_time)
    finished_at = db.Column(DateTime, onupdate=current_time)
    deleted_at = db.Column(DateTime)
    category = db.relationship("Category", backref=db.backref("tasks", lazy=True))

    def __init__(
        self,
        title,
        user_id,
        category_id,
        description=None,
    ):
        self.title = title
        self.user_id = user_id
        self.description = description
        self.category_id = category_id

    def as_dict(self):
        task_dict = {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "finished_at": self.finished_at,
            "user_id": self.user_id,
            "category_id": self.category_id,
            "category_name": self.category.name if self.category else None,
        }

        return task_dict
