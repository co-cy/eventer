from flask import Flask

from pages import create_event
from pages import index
from pages import event
from pages import registration
from pages import user
from pages import registration_organizer
from pages import organizer


def init_pages(app: Flask) -> None:
    app.register_blueprint(index.blueprint)
    app.register_blueprint(create_event.blueprint)
    app.register_blueprint(event.blueprint)
    app.register_blueprint(registration.blueprint)
    app.register_blueprint(user.blueprint)
    app.register_blueprint(registration_organizer.blueprint)
    app.register_blueprint(organizer.blueprint)
