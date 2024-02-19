from flask_jwt_extended import create_access_token
from app.models.user_model import User
from app.models.model import db
from werkzeug import security
from dotenv import load_dotenv
import os
from datetime import timedelta

load_dotenv()


def generate_access_token(user_id):
    access_token = create_access_token(identity=user_id)
    return access_token


def create_user(name, email, password):
    hashed_password = security.generate_password_hash(password, method="pbkdf2:sha256")
    new_user = User(name=name, email=email, password=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    access_token = generate_access_token(new_user.id)
    return access_token


def find_user_by_email(email):
    existing_user = User.query.filter_by(email=email).first()
    return existing_user


def find_user_by_id(user_id):
    user = User.query.filter_by(id=user_id)
    return user
