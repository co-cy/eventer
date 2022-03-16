from flask import Blueprint, render_template, abort
from database.event import Event
from flask_loguru import logger

blueprint = Blueprint("event", __name__)


@blueprint.route("/event/<int:id_event>", methods=["GET"])
@logger.catch(onerror=lambda _: abort(500))
def event(id_event: int):
    logger.info("Someone went to the event page under id - {}", id_event)
    event_obj: Event = Event.query.get(id_event)
    if event_obj:
        logger.info("The event was found id - {}", id_event)
        return render_template("event.html", event=event_obj)
    logger.info("Event was not found id - {}", id_event)
    return abort(404)
