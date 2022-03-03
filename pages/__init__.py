from pages import index
from flask import Flask


def init_pages(app: Flask) -> None:
    app.register_blueprint(index.blueprint)
