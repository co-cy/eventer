from pages import init_pages
from flask import Flask
from database import db
from forms import csrf
from flask_celery import celery
from database import event

app = Flask(__name__)
app.config.from_pyfile('server_config.py')

db.init_app(app)
with app.app_context():
    db.create_all()

csrf.init_app(app)
celery.init_app(app)

init_pages(app)


@celery.task
def delete_event2(id_event: int):
    cur_event: event.Event = event.Event.query.get(id_event)
    cur_event.is_deleted = True

    db.session.commit()