from pages import init_pages
from flask import Flask
from database import db
from forms import csrf
from flask_celery import celery

app = Flask(__name__)
app.config.from_pyfile('server_config.py')

db.init_app(app)
with app.app_context():
    db.create_all()

csrf.init_app(app)
celery.init_app(app)

init_pages(app)


@celery.task
def add(x, y):
    return x + y
