from config import FlaskConfig, SqlalchemyConfig
from flask_celery import celery
from pages import init_pages
from flask import Flask
from database import db
from forms import csrf

app = Flask(__name__)
app.config.update(**FlaskConfig(), **SqlalchemyConfig())

db.init_app(app)
with app.app_context():
    db.create_all()

csrf.init_app(app)
celery.init_app(app)

init_pages(app)
