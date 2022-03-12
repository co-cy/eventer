from flask import Blueprint, render_template
from database.event import Event
from datetime import datetime

blueprint = Blueprint("index", __name__)


@blueprint.route("/", methods=["GET"])
def index():
    events = Event.query.filter(Event.end_date >= datetime.utcnow()).all()
    return render_template("index.html", events=events)
