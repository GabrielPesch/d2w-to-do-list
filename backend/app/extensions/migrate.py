from flask_migrate import Migrate
from ..models.model import db


def init_app(app):
    db.init_app(app)
    Migrate(app, db)
    with app.app_context():
        db.create_all()
