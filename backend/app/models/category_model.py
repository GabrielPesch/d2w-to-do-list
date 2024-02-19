from .model import db
from datetime import datetime
from sqlalchemy import DateTime
import pytz


def current_time():
    sao_paulo_tz = pytz.timezone("America/Sao_Paulo")
    return datetime.now(sao_paulo_tz)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(DateTime, default=current_time)
    updated_at = db.Column(DateTime, onupdate=current_time)
    deleted_at = db.Column(DateTime)

    def __init__(self, name):
        self.name = name

    def as_dict(self):
        category_dict = {
            "id": self.id,
            "name": self.name,
        }

        return category_dict
