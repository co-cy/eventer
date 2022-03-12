from flask_celery import celery
from database import event, db


@celery.task
def delete_event(id_event: int):
    cur_event: event.Event = event.Event.query.get(id_event)
    cur_event.is_deleted = True

    db.session.commit()
