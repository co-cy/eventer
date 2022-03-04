from flask import Flask
from pages import index
from pages import create_event


def init_pages(app: Flask) -> None:
    app.register_blueprint(index.blueprint)
    app.register_blueprint(create_event.blueprint)
