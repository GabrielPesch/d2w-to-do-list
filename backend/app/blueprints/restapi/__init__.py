from .controllers.main_controller import main
from .controllers.session_controller import session
from .controllers.task_controller import task
from .controllers.category_controller import category


def init_app(app):
    app.register_blueprint(main)
    app.register_blueprint(session)
    app.register_blueprint(task)
    app.register_blueprint(category)
