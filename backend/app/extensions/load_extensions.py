from importlib import import_module


def init_app(app):
    extensions_to_load = [
        "app.extensions.cors",
        "app.extensions.jwt",
        "app.extensions.migrate",
        "app.blueprints.restapi",
        "app.extensions.error_handler",
    ]

    for extension in extensions_to_load:
        mod = import_module(extension)
        mod.init_app(app)
