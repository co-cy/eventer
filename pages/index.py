from flask import Blueprint, render_template
from database.event import Event

blueprint = Blueprint("index", __name__)


@blueprint.route("/", methods=["GET"])
def index():
    events = Event.query.filter_by(is_deleted=False).all()
    return render_template("index.html", events=events)
