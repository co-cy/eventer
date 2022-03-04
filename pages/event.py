from flask import Blueprint, render_template, abort
from database.event import Event

blueprint = Blueprint("event", __name__)


@blueprint.route("/event/<int:id_event>", methods=["GET"])
def event(id_event: int):
    event_obj: Event = Event.query.get(id_event)
    if event_obj:
        return render_template("event.html", event=event_obj)
    return abort(404)
