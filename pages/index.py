from flask import Blueprint, render_template
from database.event import Event

blueprint = Blueprint("index", __name__)


@blueprint.route("/", methods=["GET"])
def index():
    events = Event.query.all()
    return render_template("index.html", events=events)
