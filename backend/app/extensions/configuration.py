import os
from dotenv import load_dotenv

load_dotenv()


def init_app(app):
    # para executar sem o docker
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}"
        f"@{os.environ['POSTGRES_HOST']}:{os.environ['POSTGRES_PORT']}/?client_encoding=utf8"
    )

    # para executar com o docker
    # app.config["SQLALCHEMY_DATABASE_URI"] = (
    #     f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}"
    #     f"@db:{os.environ['POSTGRES_PORT']}"
    # )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = int(
        os.environ.get("JWT_ACCESS_TOKEN_EXPIRES", 3600)
    )
